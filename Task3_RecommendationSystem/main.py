import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ===============================
# 1. LOAD DATASET
# ===============================
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "tmdb_5000_movies.csv")

movies = pd.read_csv(file_path)

print("✅ Dataset loaded successfully!")

# ===============================
# 2. CLEAN DATA
# ===============================
movies['overview'] = movies['overview'].fillna('')
movies['title'] = movies['title'].fillna('')

movies['title_lower'] = movies['title'].str.lower()

# ===============================
# 3. FEATURE ENGINEERING (BETTER VERSION)
# ===============================
# Combine overview + title for stronger recommendations
movies['content'] = movies['title'] + " " + movies['overview']

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['content'])

# ===============================
# 4. SIMILARITY MATRIX
# ===============================
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

# ===============================
# 5. SMART RECOMMENDER
# ===============================
def recommend(movie_name):
    movie_name = movie_name.lower().strip()

    # flexible matching
    matches = movies[movies['title_lower'].str.contains(movie_name, na=False)]

    # if no match found
    if matches.empty:
        print("\n❌ Movie not found in dataset.")
        print("💡 Did you mean one of these?")

        # show closest matches
        suggestions = movies[movies['title_lower'].str.contains(movie_name[:3], na=False)]
        print(suggestions['title'].head(5).to_string(index=False))
        return

    index = matches.index[0]

    print("\n🎬 Selected Movie:", movies.iloc[index]['title'])

    # similarity ranking
    distances = list(enumerate(similarity[index]))
    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    print("\n🍿 Top 5 Recommendations:")
    print("-" * 40)

    for i in sorted_movies:
        print("⭐", movies.iloc[i[0]]['title'])

# ===============================
# 6. USER INTERFACE
# ===============================
print("\n🎥 Movie Recommendation System Ready!")
print("Type a movie name (or 'exit')\n")

while True:
    user_input = input("Enter movie name: ")

    if user_input.lower().strip() == "exit":
        print("👋 Goodbye! Enjoy Movies")
        break

    recommend(user_input)