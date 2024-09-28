import random
from tkinter import *
from tkinter import messagebox
import pandas as pd
from fuzzywuzzy import fuzz, process
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(index, df):
    return df.iloc[index]["title"]

def get_index_from_title(title, df):
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

def combine_features(row):
    return " ".join([row['keywords'], row['cast'], row['genres'], row['director']])

# Load data and preprocess
df = pd.read_csv("movie_dataset.xls")
features = ['keywords', 'cast', 'genres', 'director']
df[features] = df[features].fillna('')
df["combined_features"] = df.apply(combine_features, axis=1)

# Precompute cosine similarity
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)

def get_list(movie_user_likes, cosine_sim, df):
    movie_index = get_index_from_title(movie_user_likes, df)
    if movie_index == -1:
        return []
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
    return [get_title_from_index(element[0], df) for element in sorted_similar_movies[:20]]

def display_recommendations():
    for widget in bottomFrame.winfo_children():
        widget.destroy()
    
    movie = entry1.get()
    if not movie:
        messagebox.showerror("Invalid Choice", "Please enter a valid movie name")
        return

    recommended_movies = get_list(movie, cosine_sim, df)
    if not recommended_movies:
        return

    for item in recommended_movies:
        Label(bottomFrame, text=item, fg="#383127", bg="#E4DBBF").pack(side=TOP, fill=X)

# Set up GUI
root = Tk()
root.title("Movie Recommendation System")

topFrame = Frame(root)
topFrame.pack(fill=X)
Label(topFrame, text="Movie Recommendation System", fg="#000000", bg="#f5c518", font=("Roboto", 24, "bold")).pack(fill=X)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM, fill=X)

Label(root, text="Enter a movie of your choice: ").pack(side=LEFT)
entry1 = Entry(root, width=30)
entry1.pack(side=LEFT)

Button(root, text="Get recommendations", command=display_recommendations).pack(side=BOTTOM)

root.mainloop()
