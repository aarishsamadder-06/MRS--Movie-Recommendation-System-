# Movie Recommendation System

Live demo: [https://azjmxvrjtbvmrqkwv2wkdg.streamlit.app/](https://azjmxvrjtbvmrqkwv2wkdg.streamlit.app/)

This repository contains a small, deployable movie recommendation app built with Streamlit. The app loads `movies.csv`, vectorizes movie genres with TF–IDF, and recommends similar movies using cosine similarity.

## Screenshot

<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="700" viewBox="0 0 1200 700">
  <defs>
    <style>
      .bg { fill: #0e1117; }
      .card { fill: #ffffff; rx: 12px; }
      .title { fill: #0f1724; font-family: Arial, Helvetica, sans-serif; font-size: 32px; font-weight: 700; }
      .label { fill: #6b7280; font-family: Arial, Helvetica, sans-serif; font-size: 16px; }
      .btn { fill: #ff4b4b; rx: 8px; }
      .btn-txt { fill: #fff; font-family: Arial, Helvetica, sans-serif; font-size: 16px; font-weight: 700; }
      .item { fill: #0f1724; font-family: Arial, Helvetica, sans-serif; font-size: 18px; }
    </style>
  </defs>

  <rect width="1200" height="700" class="bg" />

  <g transform="translate(80,60)">
    <rect width="1040" height="580" class="card" />
    <text x="30" y="56" class="title">🎬 Movie Recommendation System</text>

    <!-- Selector -->
    <text x="40" y="120" class="label">Choose a movie</text>
    <rect x="40" y="130" width="520" height="42" fill="#f3f4f6" rx="6" />
    <text x="52" y="157" class="label">Inception</text>

    <!-- Button -->
    <rect x="580" y="130" width="140" height="42" class="btn" />
    <text x="604" y="157" class="btn-txt">Recommend</text>

    <!-- Recommendations list -->
    <text x="40" y="220" class="label">You may also like:</text>
    <g transform="translate(40,240)">
      <rect x="0" y="0" width="960" height="44" fill="#f8fafc" rx="8" />
      <text x="18" y="30" class="item">👉 Interstellar</text>
    </g>
    <g transform="translate(40,298)">
      <rect x="0" y="0" width="960" height="44" fill="#f8fafc" rx="8" />
      <text x="18" y="30" class="item">👉 The Matrix</text>
    </g>
    <g transform="translate(40,356)">
      <rect x="0" y="0" width="960" height="44" fill="#f8fafc" rx="8" />
      <text x="18" y="30" class="item">👉 Inception (again)</text>
    </g>
    <g transform="translate(40,414)">
      <rect x="0" y="0" width="960" height="44" fill="#f8fafc" rx="8" />
      <text x="18" y="30" class="item">👉 Dark</text>
    </g>

    <!-- Footer note -->
    <text x="40" y="540" class="label">Screenshot: local Streamlit UI mock (actual layout may vary)</text>
  </g>
</svg>
</p>

## Quick Start (local)

1. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open http://localhost:8501 in your browser (Streamlit prints the URL in the terminal).

## How the app works

- The web UI is implemented in `app.py`. It creates a `MovieRecommender` instance and shows a movie selector; pressing **Recommend** shows similar titles.
- Recommendation logic lives in `model.py` in the `MovieRecommender` class. Implementation summary:
  - Loads the CSV at `movies.csv` (expects columns `title` and `genre`).
  - Uses `TfidfVectorizer` on the `genre` column.
  - Computes pairwise cosine similarity and returns the top N similar titles.

## Dataset

- File: `movies.csv`
- Expected columns: `title`, `genre`.
- Example rows from the included dataset:

  ```
  title,genre
  Stranger Things,Science Fiction Thriller Horror
  Inception,Science Fiction Thriller
  The Matrix,Science Fiction Action
  Harry Potter and the Sorcerer's Stone,Fantasy Adventure
  ```

Keep `movies.csv` in the repository root so `app.py` can load it directly.

## Programmatic usage

Use the `MovieRecommender` class from `model.py` in scripts or tests:

```python
from model import MovieRecommender

recommender = MovieRecommender("movies.csv")
results = recommender.recommend("Inception", top_n=5)
print(results)
```

Parameters:
- `movie_title` (str): exact movie title as shown in the `title` column.
- `top_n` (int): number of recommendations to return (default 5).

## Deployment (Streamlit Cloud)

1. Push this repository to GitHub.
2. Go to https://streamlit.io/cloud (or the Streamlit Community Cloud) and create a new app.
3. Select your GitHub repository, branch (e.g., `main`), and set the main file to `app.py`.
4. Streamlit will use `requirements.txt` to install dependencies and deploy your app.

## Improving recommendations

- Expand features used for similarity (e.g., combine `genre` with `description`, `cast`, or metadata).
- Use more advanced embeddings (word2vec, sentence-transformers) for richer semantic similarity.
- Cache the TF–IDF matrix or precompute embeddings if dataset grows large.

## Troubleshooting

- If `movies.csv` is not found, ensure the file resides in the project root and that you run the app from the repository directory.
- If you see import errors, confirm the virtual environment is active and `pip install -r requirements.txt` completed successfully.

## Files

- `app.py` — Streamlit UI and entrypoint.
- `model.py` — `MovieRecommender` class (TF–IDF + cosine similarity).
- `movies.csv` — Example dataset (columns: `title`, `genre`).
- `requirements.txt` — Dependencies (`streamlit`, `pandas`, `scikit-learn`).

## Contributing

Contributions welcome — open an issue or submit a pull request. Suggested improvements:

- Add richer metadata and sample preprocessing pipeline.
- Add unit tests for `MovieRecommender` behavior.
- Provide Dockerfile or CI configuration for automated deployments.




