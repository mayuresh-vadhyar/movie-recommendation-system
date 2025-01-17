import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz, process
from models import CustomException

MINIMUM_THRESHOLD = 70
RECOMMENDED_MOVIES_COUNT = 20

class ContentBasedFiltering:
    def __init__(self):
        # Load data and preprocess
        print('called contentBasedFiltering')
        df = pd.read_csv("movie_dataset.xls")
        features = ['keywords', 'cast', 'genres', 'director']
        df[features] = df[features].fillna('')
        df["combined_features"] = df.apply(self.combineFeatures, axis=1)

        # Precompute cosine similarity
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(df["combined_features"])
        self.cosine_sim = cosine_similarity(count_matrix)
        self.df = df

    def combineFeatures(self, row):
        return " ".join([row['keywords'], row['cast'], row['genres'], row['director']])

    def getRecommendedMovies(self, movieIndex):
        similar_movies = list(enumerate(self.cosine_sim[movieIndex]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
        return [self.getTitleFromIndex(element[0]) for element in sorted_similar_movies[:RECOMMENDED_MOVIES_COUNT]]

    def getTitleFromIndex(self, index):
        return self.df.iloc[index]["title"]

    def getIndexFromTitle(self, title):
            titles = self.df['title'].tolist()
            closest_match = process.extractOne(title, titles, scorer=fuzz.token_sort_ratio)
            
            if len(closest_match) < 1 and closest_match[1] < MINIMUM_THRESHOLD:
                raise CustomException("MOVIE_NOT_FOUND")
            
            return self.df[self.df.title == closest_match[0]]["index"].values[0]


