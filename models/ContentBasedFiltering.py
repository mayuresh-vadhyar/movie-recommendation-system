from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from models.CustomException import CustomException
from constants import ERRORS as errors
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

    def getRecommendedMovies(self, movieIndex, pageSize = 0, pageNo = 1):
        if movieIndex < 0 or movieIndex >= len(self.cosine_sim):
            raise CustomException(errors.INVALID_INDEX)

        pageSize = pageSize or constants.RECOMMENDED_MOVIES_COUNT
        start = (pageNo - 1) * pageSize
        end = start + pageSize
        similar_movies = list(enumerate(self.cosine_sim[movieIndex]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
        paginated_movies = sorted_similar_movies[start:end]
        return [self.df.getTitleFromIndex(movie[0]) for movie in paginated_movies]