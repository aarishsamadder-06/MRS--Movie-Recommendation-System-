# Movie Recommendation System

Live demo: [https://azjmxvrjtbvmrqkwv2wkdg.streamlit.app/](https://azjmxvrjtbvmrqkwv2wkdg.streamlit.app/)

This repository contains a small, deployable movie recommendation app built with Streamlit. The app loads `movies.csv`, vectorizes movie genres with TF–IDF, and recommends similar movies using cosine similarity.

## Screenshot
<img width="1796" height="803" alt="Screenshot 2026-01-18 231020" src="https://github.com/user-attachments/assets/49e31fa4-4e61-4f82-a930-28c8540ab6cb" />



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




