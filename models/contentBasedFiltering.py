from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from models.DataFrame import DataFrame
from constants import CONTENT_BASED_FILTERING as constants
from constants import COLUMN_NAMES as columns

class ContentBasedFiltering:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            # Precompute cosine similarity
            self.df = DataFrame()
            cv = CountVectorizer()
            count_matrix = cv.fit_transform(self.df.getByColumn(columns.FEATURES))
            self.cosine_sim = cosine_similarity(count_matrix)
            self._initialized = True

    def getRecommendedMovies(self, movieIndex):
        similar_movies = list(enumerate(self.cosine_sim[movieIndex]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
        return [self.df.getTitleFromIndex(element[0]) for element in sorted_similar_movies[:constants.RECOMMENDED_MOVIES_COUNT]]



