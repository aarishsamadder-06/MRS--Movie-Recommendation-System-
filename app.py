import streamlit as st
from model import MovieRecommender

st.set_page_config(page_title="Movie Recommendation System", layout="centered")

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get similar recommendations!")

recommender = MovieRecommender("movies.csv")

movie_list = recommender.df["title"].tolist()
selected_movie = st.selectbox("Choose a movie:", movie_list)

if st.button("Recommend"):
    recommendations = recommender.recommend(selected_movie)

    if recommendations:
        st.subheader("You may also like:")
        for movie in recommendations:
            st.write("👉", movie)
    else:
        st.write("No recommendations found.")
