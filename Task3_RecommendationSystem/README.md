# Task 3 - Recommendation System

A recommendation system that suggests items based on user preferences.
# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Python, Streamlit, Pandas, and Scikit-Learn.

The application recommends similar movies based on the movie selected by the user using TF-IDF Vectorization and Cosine Similarity.

---

## 🚀 Features

- Movie recommendations based on user preferences
- Content-Based Filtering
- TF-IDF Vectorization
- Cosine Similarity Algorithm
- Interactive Streamlit Web Interface
- Top 10 Recommended Movies
- Similarity Scores
- Movie Ratings and Release Dates
- Smart Search Suggestions

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-Learn
- Streamlit

---

## 📂 Dataset

TMDB 5000 Movies Dataset

Dataset contains:
- Movie Titles
- Overviews
- Genres
- Keywords
- Ratings
- Release Dates
- Popularity Scores

---

## ⚙️ How It Works

1. User enters a movie title.
2. The system searches for the movie in the dataset.
3. Movie descriptions, genres, and keywords are converted into numerical vectors using TF-IDF.
4. Cosine Similarity is calculated between movies.
5. The system displays the Top 10 most similar movies.

---

## 📁 Project Structure

```text
Task3_RecommendationSystem/
│
├── app.py
├── tmdb_5000_movies.csv
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Divyanshi-shisodia/CODSOFT.git
```

Navigate to the project folder:

```bash
cd Task3_RecommendationSystem
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🧠 Recommendation Technique

This project uses:

- Content-Based Filtering
- TF-IDF Vectorization
- Cosine Similarity

to find movies with similar content and recommend them to the user.

---

## 📸 Screenshots:
<img width="959" height="506" alt="Screenshot 2026-06-08 232908" src="https://github.com/user-attachments/assets/8b24195c-741e-448b-ab01-739cb9a78fa3" />




Example:

- Home Page
- Recommendation Results

---

## 🎯 Future Improvements

- Movie Posters
- Genre-Based Recommendations
- Search History
- Trending Movies Section
- Enhanced UI Design

---

## 👩‍💻 Author

Divyanshi Shisodia

CodSoft Internship Project
