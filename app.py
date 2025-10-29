import csv
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Cuisine Normalization 
CUISINE_ALIASES = {
    # Mediterranean & neighbors
    "mediterranean": "mediterranean",
    "greek": "greek",
    "greece": "greek",
    "turkish": "turkish",
    "turkey": "turkish",
    "italian": "italian",
    "italy": "italian",
    "spanish": "spanish",
    "spain": "spanish",

    # Middle Eastern
    "middle eastern": "middle eastern",
    "persian": "persian",
    "iran": "persian",
    "iranian": "persian",
    "lebanese": "lebanese",
    "israeli": "israeli",
    "arabic": "arabic",

    # Asian (East, South, SE)
    "asian": "asian",
    "japanese": "japanese",
    "japan": "japanese",
    "korean": "korean",
    "korea": "korean",
    "chinese": "chinese",
    "china": "chinese",
    "thai": "thai",
    "vietnamese": "vietnamese",
    "vietnam": "vietnamese",
    "indian": "indian",
    "india": "indian",

    # Latin American
    "latin american": "latin american",
    "mexican": "mexican",
    "mexico": "mexican",
    "peruvian": "peruvian",
    "peru": "peruvian",
    "brazilian": "brazilian",
    "brazil": "brazilian",
    "argentinian": "argentinian",
    "argentina": "argentinian",

    # Other common
    "french": "french",
    "german": "german",
    "british": "british",
    "american": "american",
}

def canonical_cuisine(name: str) -> str:
    if not name:
        return ""
    name = name.strip().lower()
    return CUISINE_ALIASES.get(name, name)

# Data Loading 
def to_float(v, default=0.0):
    try:
        return float(v)
    except Exception:
        return default

def load_recipes(path="data/recipes.csv"):
    items = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append({
                "title": (row.get("title") or "").strip(),
                "diet": (row.get("diet") or "").strip().lower(),  # '', 'vegan', 'vegetarian'
                "cuisine": canonical_cuisine(row.get("cuisine") or ""),
                "ingredients": (row.get("ingredients") or "").lower(),
                "allergens": (row.get("allergens") or "").lower(),
                "summary": row.get("summary") or "",
                "url": (row.get("url") or "").strip(),
                "calories": to_float(row.get("calories")),
                "protein_g": to_float(row.get("protein_g")),
                "fiber_g": to_float(row.get("fiber_g")),
            })
    return items

RECIPES = load_recipes()

# Scoring 
GOAL_WEIGHTS = {
    "balanced":     {"protein_g": 0.6, "fiber_g": 0.4},
    "weight_loss":  {"fiber_g": 0.7, "protein_g": 0.3},
    "muscle_gain":  {"protein_g": 1.0, "fiber_g": 0.2},
}

def score_recipe(recipe: dict, goal: str) -> float:
    w = GOAL_WEIGHTS.get(goal or "balanced", GOAL_WEIGHTS["balanced"])
    return round((recipe.get("protein_g", 0) or 0) * w["protein_g"] +
                 (recipe.get("fiber_g", 0) or 0) * w["fiber_g"], 2)

# Family Buckets 
def family_match(requested: str, rc: str) -> bool:
    """Allow family buckets such as Mediterranean, Asian, Latin American."""
    if requested == rc:
        return True
    fams = {
        "mediterranean": {"greek", "turkish", "italian", "spanish"},
        "asian": {"japanese", "korean", "chinese", "thai", "vietnamese", "indian"},
        "middle eastern": {"persian", "lebanese", "israeli", "arabic", "turkish"},
        "latin american": {"mexican", "peruvian", "brazilian", "argentinian"},
    }
    return rc in fams.get(requested, set())

# Build List 
def build_list(diet="", cuisine="", excludes=None, goal="balanced"):
    excludes = [e.strip().lower() for e in (excludes or []) if e.strip()]
    out = []
    for r in RECIPES:
        # Diet filter (only if chosen)
        if diet and r["diet"] and r["diet"] != diet:
            continue

        # Cuisine filter (only if chosen)
        if cuisine:
            rc = r["cuisine"]
            if not family_match(cuisine, rc):
                continue

        # Exclusions
        if excludes:
            hay = f"{r['ingredients']} {r['allergens']}"
            if any(term in hay for term in excludes):
                continue

        rr = dict(r)
        rr["score"] = score_recipe(r, goal)
        out.append(rr)

    out.sort(key=lambda x: (-x["score"], x["title"]))
    return out

# Routes 
@app.route("/", methods=["GET", "POST"])
def index():
    # SHOW NOTHING on first load (recipes=None)
    if request.method == "GET":
        return render_template("index.html", recipes=None)

    # POST: apply filters
    diet = (request.form.get("diet") or "").strip().lower()
    goal = (request.form.get("goal") or "balanced").strip().lower()
    cuisine = canonical_cuisine(request.form.get("cuisine") or "")
    exclude_raw = (request.form.get("exclude") or "").strip().lower()
    excludes = [x for x in exclude_raw.split(",") if x.strip()]

    # First pass: use exactly what the user selected
    recipes = build_list(diet=diet, cuisine=cuisine, excludes=excludes, goal=goal)

    # IMPORTANT CHANGE:
    # Only relax results if the user did NOT choose a cuisine.
    # If a specific cuisine was chosen (e.g., "italian"), keep it strict.
    if (not cuisine) and len(recipes) < 15:
        relaxed = build_list(diet=diet, cuisine="", excludes=excludes, goal=goal)
        have = {x["title"] for x in recipes}
        recipes += [x for x in relaxed if x["title"] not in have]

    return render_template("index.html", recipes=recipes)

# Run 
if __name__ == "__main__":
    # 0.0.0.0 so Codespaces/containers can preview
    app.run(host="0.0.0.0", port=5000, debug=True)
