import pandas as pd
from fuzzywuzzy import fuzz, process
from models.CustomException import CustomException
from constants import CONTENT_BASED_FILTERING as constants
from constants import COLUMN_NAMES as columns
from constants import ERRORS as errors

class DataFrame():
    _instance = None
    _df = None

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

            self._df = df
            self._initialized = True

    def combineFeatures(self, row):
        return " ".join([row[column] for column in constants.FILTER_COLUMNS])

    def getTitleFromIndex(self, index):
        return self._df.iloc[index][columns.TITLE]

    def getByColumn(self, title):
        return self._df[title]

    def getIndexFromTitle(self, title):
        return self._df[self._df[columns.TITLE] == title]["index"].values[0]

    def getIndexOfClosestTitle(self, title):
        titles = self._df[columns.TITLE].tolist()
        closest_match = process.extractOne(title, titles, scorer=fuzz.token_sort_ratio)

        if len(closest_match) < 1:
            raise CustomException(errors.MOVIE_NOT_FOUND)

        if closest_match[1] < constants.MINIMUM_THRESHOLD:
            raise CustomException(errors.MOVIE_NOT_FOUND)
        
        return self._df[self._df[columns.TITLE] == closest_match[0]]["index"].values[0]