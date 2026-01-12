import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df["genre"])
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)

    def recommend(self, movie_title, top_n=5):
        if movie_title not in self.df["title"].values:
            return []

        index = self.df[self.df["title"] == movie_title].index[0]
        scores = list(enumerate(self.similarity_matrix[index]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        recommendations = []
        for i in scores[1:top_n + 1]:
            recommendations.append(self.df.iloc[i[0]]["title"])

        return recommendations
