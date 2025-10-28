# Grenbi Lite — CS50 Final Project  
#### Video Demo: https://youtu.be/_wBSkWtD4j8?si=laXPhFBx9ep9SPKI
Author: **Soroush Aliasghari Namin**  
GitHub: [@soroushnamin](https://github.com/soroushnamin)  
City/Country: **Istanbul, Turkey**  
Date: **October 2025**

---
#### Description:

## Overview  
Grenbi Lite is a simplified version of my startup project, Grenbi AI.  
It was built from scratch for the CS50 Final Project using Python and Flask.  
The goal of this project is to demonstrate how personalized recipe suggestions can be made based on a user’s diet type, health goals, and cuisine preferences.  

In the real Grenbi AI, this system is much more advanced and connects with DNA, microbiome, and blood test data. But this version focuses on the core logic and algorithms that make those personalized recommendations possible.  

Grenbi Lite runs as a simple web app built with Flask, using a CSV file to load recipe data.  
It allows users to choose a diet (vegan or vegetarian), set a health goal (balanced, weight loss, or muscle gain), type in any cuisine or country, and exclude allergens or ingredients they don’t want.  
It then filters and ranks the recipes based on nutritional balance and relevance.

---

## Technologies Used  
- Python 3  
- Flask  
- HTML and CSS with Jinja templates  
- CSV file handling (using Python’s built-in `csv` library)  
- Pathlib and Unicodedata for file and text normalization  

No external data analysis library like Pandas is used. The recipe filtering and ranking are done manually in Python to show full control of the code and logic.

---

## Project Structure  
```
Grenbi-Student-CS50-final-project/
│
├── app.py               # Main Flask application
├── data/
│   └── recipes.csv       # Recipe dataset
├── templates/
│   └── index.html        # Front-end HTML template
├── static/
│   └── style.css         # Styling and layout
└── README.md             # Project documentation
```

---

## How It Works  

When the app starts, Flask loads the recipe dataset from `data/recipes.csv`.  
Each recipe includes fields such as title, diet, cuisine, calories, protein, fiber, allergens, and summary.  

Users fill out a short form on the main page where they can:  
- Select a diet type (vegan, vegetarian, or any)  
- Choose a goal (balanced, weight loss, or muscle gain)  
- Type any cuisine or country (for example: Turkish, Persian, Indian, Mediterranean)  
- Exclude ingredients or allergens  

After submitting, Flask filters and ranks recipes that best match the user’s preferences and goals.  
Each result shows the recipe name, nutritional data, and a simple health score based on calories, protein, and fiber.  
At the end of each recipe card, there is a link to Grenbi.com for users to visit and see more details.

---

## Main Features and Functions  

### app.py  
This file contains all the logic and routes of the web app.

**Key functions:**  
- `_norm(s)` – Normalizes text by removing extra spaces, accents, and converting to lowercase.  
- `expand_cuisine_terms()` – Matches country names to cuisine types. For example, “Iran” becomes “Persian”, and “Turkey” becomes “Turkish”.  
- `_load_raw_list()` – Loads and cleans data from the CSV file.  
- `build_filtered_list()` – Filters recipes by diet, cuisine, and excluded ingredients.  
- `nutrition_score()` – Calculates a simple score based on the selected goal and recipe nutrition.  
- `rank_recipes()` – Sorts the final results by their score and nutrition quality.  
- `index()` – The main Flask route that handles user requests and displays results.

The logic is modular so that the same code could later be connected to a database or API.

---

### index.html  
The main interface for the user.  
It includes the form where users enter their diet, goal, cuisine, and exclusions.  
It also displays results dynamically using Jinja templating.  

Each recipe card shows:  
- Recipe title  
- Calories, protein, and fiber values  
- Health score  
- Cuisine type  
- A button linking to grenbi.com for more details

---

### style.css  
The design follows a simple and clean layout with a green theme that matches the Grenbi brand.  
Cards are rounded, easy to read, and adapt well to different screen sizes.  
This design choice was made to keep focus on the recipe data and the user experience.

---

## Design Choices  

1. **Manual CSV parsing**  
   I used Python’s `csv` library instead of Pandas to keep the logic simple and transparent.  

2. **Flask instead of Django**  
   Flask provides a lightweight framework for small projects, making it ideal for CS50’s environment.  

3. **Scoring logic**  
   A rule-based scoring system was implemented to show how an algorithm can estimate which meals are better for different goals.  

4. **Flexible cuisine search**  
   The app can understand country names or cuisine families and suggest related recipes.  

5. **Fallbacks**  
   If there are no perfect matches, the app still shows close results so users never get an empty page.

---

## Reflection  

This project helped me understand how to combine Python with web technologies to build a working app.  
I learned how to handle user inputs, process data, and return results dynamically with Flask.  
I also practiced modular code design and how to normalize data for real-world usability.  

If I continue developing Grenbi Lite, I would add user accounts, more datasets, and connect it with APIs for real recipe sources.  
It could also include real-time nutritional analysis or AI-based personalization in the future.

---

## Academic Honesty  

This project was created by Soroush Aliasghari Namin as part of the CS50 final project.  
Some parts of the basic structure and documentation were written with general AI tools to help with formatting and organization.  
All ideas, code logic, design, and data used in this project were developed, customized, and tested by me personally, following CS50’s Academic Honesty policy.
