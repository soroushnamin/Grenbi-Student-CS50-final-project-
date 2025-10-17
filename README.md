# Grenbi Lite (Student-First)
#### Video Demo: <URL HERE>
#### Description:
**Grenbi Lite** is my final project for **CS50x**, inspired by my startup idea, **Grenbi** — an AI-assisted nutritionist and plant-based meal recommender.  
This lightweight web app helps users find **personalized vegetarian and vegan recipes** based on their **diet**, **nutrition goal**, **preferred cuisine**, and **allergens**.

Unlike the earlier limited demo, this version allows users to search for **any cuisine worldwide** (e.g., Persian, Mexican, Korean, Greek, Thai, etc.) — showing how Grenbi’s concept can adapt to every culture and food preference.

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

### 🧩 File Structure
