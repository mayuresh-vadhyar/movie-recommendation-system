import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz, process

class contentBasedFiltering:
    def __init__(self):
        # Load data and preprocess
        df = pd.read_csv("movie_dataset.xls")
        features = ['keywords', 'cast', 'genres', 'director']
        df[features] = df[features].fillna('')
        df["combined_features"] = self.df.apply(combineFeatures, axis=1)

        # Precompute cosine similarity
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(self.df["combined_features"])
        self.cosine_sim = cosine_similarity(count_matrix)
        self.df = df

    def combineFeatures(self, row):
        return " ".join([row['keywords'], row['cast'], row['genres'], row['director']])

    def getList(self, movie_user_likes, df):
        movie_index = self.getIndexFromTitle(movie_user_likes, df)
        if movie_index == -1:
            return []
        similar_movies = list(enumerate(self.cosine_sim[movie_index]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
        return [self.getTitleFromIndex(element[0], df) for element in sorted_similar_movies[:20]]

    
    def getTitleFromIndex(self, index, df):
        return df.iloc[index]["title"]

    def getIndexFromTitle(self, title, df):
        try:
            titles = df['title'].tolist()
            closest_match = process.extractOne(title, titles, scorer=fuzz.token_sort_ratio)
            
            # You can define a threshold for minimum similarity
            if closest_match[1] >= 70:  # A threshold of 70% similarity
                return df[df.title == closest_match[0]]["index"].values[0]
            else:
                messagebox.showerror("No Match", "No similar movie found. Please try again.")
                return -1
        except IndexError:
            messagebox.showerror("Invalid Choice", "Please enter a valid movie name")
            return -1


