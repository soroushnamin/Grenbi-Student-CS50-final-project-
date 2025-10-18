"""
Grenbi Lite (Student-First),  CS50 Final Project
Author: Soroush Aliasghari Namin
GitHub: https://github.com/soroushnamin/grenbi-lite-student-first
edX: soroushnamin
City/Country: Istanbul, Turkey
Date: 17 October 2025

Academic Honesty / AI Disclosure:
- Scaffold ideas were assisted by ChatGPT (2025).
- I (Soroush) implemented the core filtering, scoring, and ranking logic.
"""

from flask import Flask, render_template, request
from pathlib import Path
import csv

app = Flask(__name__)
DATA_PATH = Path(__file__).parent / "data" / "recipes.csv"

def _load_raw_list():
    rows = []
    if not DATA_PATH.exists():
        return rows
    with open(DATA_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            r = {k: (v or "").strip() for k, v in r.items()}
            for num in ("calories", "protein_g", "fiber_g"):
                try:
                    r[num] = float(r[num])
                except Exception:
                    r[num] = 0.0
            for txt in ("diet", "cuisine", "allergens", "tags", "title", "summary"):
                r[txt] = (r.get(txt, "") or "").lower()
            rows.append(r)
    return rows

def nutrition_score(row, goal):
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
    else:
        score += 10 if (400 <= cal <= 700) else 0
        score += min(protein, 35) / 3
        score += min(fiber, 15) / 3
    return round(score, 2)

def build_filtered_list(lst, *, diet, cuisine, exclude):
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
    for r in lst:
        r["score"] = nutrition_score(r, goal)
    return sorted(lst, key=lambda r: (r["score"], r.get("protein_g", 0), r.get("fiber_g", 0)), reverse=True)

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
    return render_template("index.html", recipes=recipes)

if __name__ == "__main__":
    app.run(debug=True)
