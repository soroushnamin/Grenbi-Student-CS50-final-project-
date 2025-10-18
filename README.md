# Grenbi Lite 
**Author:** Soroush Aliasghari Namin  
**GitHub:** [github.com/soroushnamin/grenbi-lite-student-first](https://github.com/soroushnamin/grenbi-lite-student-first)  
**edX Username:** soroushnamin  
**City/Country:** Istanbul, Turkey 
**Date:** October 2025

#### Video Demo: <URL HERE>
#### Description:
**Grenbi Lite** is my final project for **CS50x**, inspired by my startup idea, **Grenbi**, an AI-assisted nutritionist and plant-based meal recommender.  
This lightweight web app helps users find **personalized vegetarian and vegan recipes** based on their **diet**, **nutrition goal**, **preferred cuisine**, and **allergens**.

Unlike the earlier limited demo, this version allows users to search for **any cuisine worldwide** (e.g., Persian, Mexican, Korean, Greek, Thai, etc.) showing how Grenbi’s concept can adapt to every culture and food preference.

---

### What It Does
Users can:
- Choose **Diet:** Vegan or Vegetarian  
- Choose **Goal:** Balanced, Weight Loss, or Muscle Gain  
- Type **Any Cuisine:** e.g., Persian, Turkish, Mexican, Japanese, Greek, etc.  
- Optionally **Exclude Allergens or Ingredients** (like gluten, peanut, soy)

The app then:
- Filters recipes from a dataset (`data/recipes.csv`)  
- Calculates a **nutrition score** based on calories, protein, and fiber  
- Ranks and displays personalized suggestions  

---

### Technologies Used
- **Python** and **Flask** for backend logic  
- **Pandas** for data filtering and scoring  
- **HTML5 + CSS3** for the front-end interface  
- **CSV** dataset containing diverse cuisines and nutritional data  

---

### What I Personally Implemented
I (Soroush) implemented the **core logic and personalization algorithms**, including:
- `nutrition_score(row, goal)` → A custom heuristic to calculate a nutrition score  
- `build_filtered_df(df, diet, cuisine, exclude)` → Filters by user preferences  
- `rank_recipes(df, goal)` → Sorts results by score and nutrient density  

These are marked with `TODO(Soroush)` in `app.py` to clearly show that I personally designed and implemented them.  
The Flask structure and UI skeleton were adapted from a base scaffold (cited per CS50’s AI policy).

---

### File Structure
grenbi-lite-student-first/
├─ app.py # Flask app + core logic
├─ requirements.txt # Flask + Pandas dependencies
├─ data/
│ └─ recipes.csv # Extended dataset with global cuisines
├─ templates/
│ └─ index.html # Front-end HTML (now with free text cuisine input)
├─ static/
│ └─ style.css # Dark, minimalist UI
├─ tests/
│ └─ test_scoring.py # Sanity tests for scoring/ranking logic
└─ README.md # This file (documentation)

---

### How to Run Locally
1. Clone or download this repository  
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # (macOS/Linux)
   # or
   .venv\Scripts\activate      # (Windows)

 ---

3. Install dependencies:

pip install -r requirements.txt


4. Run the app:

python app.py


5. Open your browser at http://127.0.0.1:5000

 ---

 ### 🧪 Optional Testing

You can verify that the logic works using:
pytest -q

 ---

### Academic Honesty & AI Disclosure

This project was built as part of CS50x (Harvard University).
I used ChatGPT only for boilerplate and project structure ideas.
All core logic, scoring design, data curation, and reasoning belong to me.
AI assistance is cited transparently in the code comments as per CS50 policy.

Submission Checklist

 Implemented custom logic (nutrition_score, filtering, ranking)

 Extended dataset with global cuisines

 Updated README.md

 Record a ≤ 3-minute demo video (include intro info)

 Add the video link above (<URL HERE>)

 Submit via:

submit50 cs50/problems/2025/x/project


 Verify completion at https://cs50.me/cs50x

---

### Credits

Author: Soroush Aliasghari Namin

Concept inspired by my AI nutrition startup, Grenbi

Dataset and recipes curated and customized for this CS50 submission

UI & design influenced by modern health-tech apps

🏁 Future Enhancements

Replace CSV with a SQL database (to demonstrate CS50 SQL skills)

Add user registration and saved preferences

Integrate AI-generated recipe recommendations via API

Display macronutrient breakdown and energy balance over time

