# Grenbi Lite
#### Video Demo: <URL HERE>
#### Description:
**Grenbi Lite** is a minimal, CS50-style prototype of my startup concept, **Grenbi** — an AI‑assisted nutritionist and vegetarian/vegan recipe recommender. This project focuses on a lightweight web application that suggests plant‑based meals tailored to user preferences (diet, goal, cuisine) while excluding allergens or disliked ingredients. It demonstrates end‑to‑end fundamentals covered in CS50: Python, data handling (CSV), basic scoring logic, and a web front‑end with HTML/CSS.

### What the App Does
Users choose:
- **Diet:** Vegan or Vegetarian
- **Goal:** Balanced, Weight Loss, or Muscle Gain
- **Cuisine:** Turkish, Indian, Italian, Asian
- **Exclude:** Any allergens or disliked items (e.g., gluten, peanut, soy)

Upon submission, the app filters a small dataset of recipes (`data/recipes.csv`) and ranks them with a simple heuristic **nutrition score** that prioritizes calories, protein, and fiber depending on the user’s goal. The top results are shown with calories, protein, fiber, and an overall score.

### Why This Matters
This prototype captures the essence of Grenbi: *personalized nutrition that respects dietary choices and taste*. While simplified and offline (no external APIs), it establishes a clean foundation for future expansion (user accounts, richer datasets, macro targets, AI‑generated plans).

### How It Works (High-Level)
- **Flask (Python)** serves the app and handles form submissions.
- **Pandas** loads and filters `recipes.csv`.
- A simple **scoring function** adapts to the selected goal:
  - *Weight Loss:* favors ≤ 500 kcal and higher protein/fiber.
  - *Muscle Gain:* favors 400–800 kcal and higher protein.
  - *Balanced:* favors 400–700 kcal and moderate protein/fiber.
- **HTML/CSS** renders a clean, dark UI with cards and badges.

### File Structure
```
grenbi-lite-cs50/
├─ app.py                # Flask app with filtering + scoring
├─ requirements.txt      # Flask + pandas
├─ data/
│  └─ recipes.csv        # Small demo dataset
├─ templates/
│  └─ index.html         # Single-page UI
└─ static/
   └─ style.css          # Minimal styling
```

### How to Run (Local)
1. **Python 3.10+** recommended.
2. Create a virtual environment:
   ```bash
   python3 -m venv .venv && source .venv/bin/activate  # macOS/Linux
   # or on Windows:
   # py -3 -m venv .venv && .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   python app.py
   ```
5. Open your browser at **http://127.0.0.1:5000**.

### Design Choices
- **CSV dataset** keeps the project portable and simple for grading, avoiding external APIs or databases.
- **Heuristic scoring** is intentionally transparent and short to review; weights can be tuned later.
- **Single template** reduces complexity while still demonstrating form handling, filtering, sorting, and rendering.
- **Dark UI** aligns with a modern aesthetic suitable for demos and screencasts.

### Possible Enhancements
- Replace CSV with **SQLite + SQL** to demonstrate queries (aligning with CS50’s SQL portion).
- Add user **macro targets** (e.g., protein grams/day) and dynamic plan generation.
- Integrate **simple ML** for personalized scoring (e.g., logistic regression on preferences).
- Add **unit tests** and input validation.
- Add **Dockerfile** for reproducible deployment.

### Academic Honesty & AI Use
- This scaffold (structure and boilerplate) was assisted by ChatGPT (2025). All customization, dataset curation, scoring, and final implementation for submission are mine. Any further AI assistance will be **cited in code comments** per CS50 policy.

### Submission Checklist (CS50x 2025)
- [ ] Record a **≤ 3‑minute** demo video (include required intro info)
- [ ] Update **README.md** with video URL + full description (aim ≈ 750 words)
- [ ] Ensure `app.py`, `templates/`, `static/`, and `data/` are present
- [ ] Push to GitHub or keep locally for `submit50`
- [ ] Run:
  ```bash
  submit50 cs50/problems/2025/x/project
  ```
- [ ] Open **https://cs50.me/cs50x** (Gradebook) to trigger certificate processing

### Credits
- Dataset entries authored for demo purposes. Nutritional values are approximate for demonstration only.
- CS50 staff and materials inspired the structure and submission process.