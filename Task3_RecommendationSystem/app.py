import streamlit as st
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Recommendation System")
st.write("Get movie recommendations using Content-Based Filtering")

# -----------------------------
# Load Dataset
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "tmdb_5000_movies.csv")

movies = pd.read_csv(file_path)

# -----------------------------
# Data Cleaning
# -----------------------------
movies['title'] = movies['title'].fillna('')
movies['overview'] = movies['overview'].fillna('')
movies['keywords'] = movies['keywords'].fillna('')
movies['genres'] = movies['genres'].fillna('')

# Combine features
movies['content'] = (
    movies['overview'] + ' ' +
    movies['genres'] + ' ' +
    movies['keywords']
)

# -----------------------------
# TF-IDF & Similarity
# -----------------------------
tfidf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tfidf.fit_transform(movies['content'])

similarity = cosine_similarity(tfidf_matrix)

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(movie_name):

    matches = movies[
        movies['title'].str.contains(
            movie_name,
            case=False,
            na=False
        )
    ]

    if matches.empty:
        return None

    index = matches.index[0]

    distances = list(enumerate(similarity[index]))

    recommended = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )[1:11]

    return recommended, index

# -----------------------------
# User Input
# -----------------------------
movie_name = st.text_input(
    "Enter a movie name",
    placeholder="Example: Avatar"
)

if st.button("Recommend"):

    result = recommend(movie_name)

    if result is None:

        st.error("Movie not found.")

        suggestions = movies[
            movies['title'].str.contains(
                movie_name[:3],
                case=False,
                na=False
            )
        ]['title'].head(5)

        if len(suggestions) > 0:
            st.write("Did you mean:")
            for movie in suggestions:
                st.write("•", movie)

    else:

        recommendations, index = result

        st.success(
            f"Recommendations based on: {movies.iloc[index]['title']}"
        )

        st.subheader("Top 10 Recommended Movies")

        for rank, movie in enumerate(recommendations, start=1):

            movie_index = movie[0]

            title = movies.iloc[movie_index]['title']

            rating = movies.iloc[movie_index]['vote_average']

            release_date = movies.iloc[movie_index]['release_date']

            score = round(movie[1] * 100, 2)

            st.markdown(
                f"""
**{rank}. {title}**

⭐ Rating: {rating}  
📅 Release Date: {release_date}  
🎯 Similarity Score: {score}%  

---
"""
            )

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Project Info")

st.sidebar.info(
    """
Movie Recommendation System

Algorithm:
- Content-Based Filtering
- TF-IDF Vectorization
- Cosine Similarity

Dataset:
TMDB 5000 Movies Dataset
"""
)