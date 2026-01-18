import streamlit as st
import pandas as pd
import os
from model import MovieRecommender

# Configuration
st.set_page_config(page_title="Movie Recommender", layout="wide")

def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# File paths
BASE_DIR = os.path.dirname(__file__)
MOVIES_PATH = os.path.join(BASE_DIR, "movies.csv")
USERS_PATH = os.path.join(BASE_DIR, "users.csv")
FEEDBACK_PATH = os.path.join(BASE_DIR, "feedback.csv")

# Load data and model
movies_df = pd.read_csv(MOVIES_PATH)
recommender = MovieRecommender(MOVIES_PATH)

# Session state for authentication
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = ""

# Authentication Functions
def login(username, password):
    users = pd.read_csv(USERS_PATH)
    return ((users["username"] == username) & (users["password"] == password)).any()

def signup(username, password):
    users = pd.read_csv(USERS_PATH)
    if username in users["username"].values:
        return False
    users.loc[len(users)] = [username, password]
    users.to_csv(USERS_PATH, index=False)
    return True

# UI
st.title("🎬 Movie Recommendation System")

if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(["🔑 Login", "📝 Sign Up"])

    with tab1:
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("Login"):
            if login(u, p):
                st.session_state.logged_in = True
                st.session_state.user = u
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        u = st.text_input("New Username")
        p = st.text_input("New Password", type="password")
        if st.button("Create Account"):
            if signup(u, p):
                st.success("Account created! Login now.")
            else:
                st.warning("Username already exists")

else:
    st.success(f"Welcome, {st.session_state.user} 👋")

    # Movie Selection and Recommendation
    selected_movie = st.selectbox("Choose a movie", movies_df["title"].tolist())

    if st.button("🎯 Recommend"):
        recs = recommender.recommend(selected_movie, top_n=5)

        st.subheader("Recommended for you")
        cols = st.columns(5)

        for col, movie in zip(cols, recs):
            with col:
                st.markdown(
                    f"""
                    <div class="movie-card">
                        <img src="https://via.placeholder.com/150x220?text={movie.replace(' ', '+')}" width="150">
                        <p>{movie}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # Feedback Section
    # ---------- FEEDBACK ----------
st.subheader("💬 Feedback")
feedback = st.text_area("Tell us what you think")

if st.button("Submit Feedback"):
    if os.path.exists(FEEDBACK_PATH) and os.path.getsize(FEEDBACK_PATH) > 0:
        df = pd.read_csv(FEEDBACK_PATH)
    else:
        df = pd.DataFrame(columns=["username", "feedback"])

    df.loc[len(df)] = [st.session_state.user, feedback]
    df.to_csv(FEEDBACK_PATH, index=False)

    st.success("Thanks for your feedback ❤️")


