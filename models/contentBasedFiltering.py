import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz, process
from constants import CONTENT_BASED_FILTERING as constants
from constants import COLUMN_NAMES as columns
from models.CustomException import CustomException


class ContentBasedFiltering:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        # Load data and preprocess
        if not self._initialized:
            df = pd.read_csv("movie_dataset.xls")
            features = constants.FILTER_COLUMNS
            df[features] = df[features].fillna('')
            df[columns.FEATURES] = df.apply(self.combineFeatures, axis=1)

            # Precompute cosine similarity
            cv = CountVectorizer()
            count_matrix = cv.fit_transform(df[columns.FEATURES])
            self.cosine_sim = cosine_similarity(count_matrix)
            self.df = df
            self._initialized = True

    def combineFeatures(self, row):
        return " ".join([row[column] for column in constants.FILTER_COLUMNS])

    def getRecommendedMovies(self, movieIndex):
        similar_movies = list(enumerate(self.cosine_sim[movieIndex]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
        return [self.getTitleFromIndex(element[0]) for element in sorted_similar_movies[:constants.RECOMMENDED_MOVIES_COUNT]]

    def getTitleFromIndex(self, index):
        return self.df.iloc[index][columns.TITLE]

    def getIndexFromTitle(self, title):
            titles = self.df[columns.TITLE].tolist()
            closest_match = process.extractOne(title, titles, scorer=fuzz.token_sort_ratio)

            if len(closest_match) < 1:
                raise CustomException("MOVIE_NOT_FOUND")

            if closest_match[1] < constants.MINIMUM_THRESHOLD:
                raise CustomException("MOVIE_NOT_FOUND")
            
            return self.df[self.df.title == closest_match[0]]["index"].values[0]


