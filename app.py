"""
Grenbi Lite - CS50 Final Project
Author: Soroush Aliasghari Namin
GitHub: soroushnamin
edX: soroushnamin
City/Country: Istanbul, Turkey
Date: 17/10/2025

Notes on AI assistance:
- Portions of this scaffold (project structure, boilerplate code, and comments) were assisted by ChatGPT in 2025.
- All 

from flask import Flask, render_template, request
from pathlib import Path
import csv

app = Flask(__name__)
DATA_PATH = Path(__file__).parent / "data" / "recipes.csv"

def _load_raw_list():
    """Load recipes from CSV into a list of dicts, with types normalized."""
    rows = []
    if not DATA_PATH.exists():
        return rows
    with open(DATA_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            r = {k: (v or "").strip() for k, v in r.items()}
            # cast numeric fields
            for num in ("calories", "protein_g", "fiber_g"):
                try:
                    r[num] = float(r[num])
                except Exception:
                    r[num] = 0.0
            # normalize text fields to lowercase for matching
            for txt in ("diet", "cuisine", "allergens", "tags", "title", "summary"):
                r[txt] = (r.get(txt, "") or "").lower()
            rows.append(r)
    return rows

def all_cuisines():
    """Return a sorted list of unique cuisines (lowercase) from the CSV."""
    seen = set()
    if DATA_PATH.exists():
        with open(DATA_PATH, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                c = (r.get("cuisine") or "").strip().lower()
                if c:
                    seen.add(c)
    return sorted(seen)

def nutrition_score(row, goal):
    """Simple heuristic you can tweak."""
    cal = row.get("calories", 0.0) or 0.0
    protein = row.get("protein_g", 0.0) or 0.0
    fiber = row.get("fiber_g", 0.0) or 0.0

    score = 0.0
    if goal == "weight_loss":
        score += 10 if cal <= 500 else 0
        score += min(protein, 30) / 3
        score += min(fiber, 15) / 3
    elif goal == "muscle_gain":
        score += 10 if (400 <= cal <= 800) else 0
        score += min(protein, 50) / 2
        score += min(fiber, 15) / 5
    else:  # balanced
        score += 10 if (400 <= cal <= 700) else 0
        score += min(protein, 35) / 3
        score += min(fiber, 15) / 3

    return round(score, 2)

def build_filtered_list(lst, *, diet, cuisine, exclude):
    """Filter by diet/cuisine substrings and exclude allergens substring."""
    out = []
    for r in lst:
        if diet and diet not in r.get("diet", ""):
            continue
        if cuisine and cuisine not in r.get("cuisine", ""):
            continue
        if exclude and exclude in r.get("allergens", ""):
            continue
        out.append(r)
    return out

def rank_recipes(lst, goal):
    """Attach 'score' and sort by score, then protein and fiber (desc)."""
    for r in lst:
        r["score"] = nutrition_score(r, goal)
    return sorted(
        lst,
        key=lambda r: (r["score"], r.get("protein_g", 0.0), r.get("fiber_g", 0.0)),
        reverse=True,
    )

@app.route("/", methods=["GET", "POST"])
def index():
    recipes = []
    if request.method == "POST":
        diet = (request.form.get("diet") or "").lower().strip()
        cuisine = (request.form.get("cuisine") or "").lower().strip()
        goal = (request.form.get("goal") or "balanced").lower().strip()
        exclude = (request.form.get("exclude") or "").lower().strip()

        base = _load_raw_list()
        filtered = build_filtered_list(base, diet=diet, cuisine=cuisine, exclude=exclude)
        recipes = rank_recipes(filtered, goal)

    return render_template("index.html", recipes=recipes, cuisines=all_cuisines())

if __name__ == "__main__":
    app.run(debug=True)
