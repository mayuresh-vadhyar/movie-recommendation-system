import random
from tkinter import *
from tkinter import messagebox
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    try:
        return df[df.title == title]["index"].values[0]
    except:
        messagebox.showerror("Invalid Choice", "Please enter a valid movie name")
        return -1

df = pd.read_csv("movie_dataset.xls")
features = ['keywords', 'cast', 'genres', 'director']
for feature in features:
    df[feature] = df[feature].fillna('')

def combine_features(row):
    try:
        return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"]
    except:
        print("Error:", row)

def get_list(movie_user_likes):
    df["combined_features"] = df.apply(combine_features, axis=1)
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    movie_index = get_index_from_title(movie_user_likes)
    if movie_index== -1:
        return
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
    list1 = []
    i = 0
    for element in sorted_similar_movies:
        list1.append(get_title_from_index(element[0]))
        i = i + 1
        if i > 20:
            break
    return list1

def getrec():
    for widget in bottomFrame.winfo_children():
        widget.destroy()
    movie = entry1.get()
    if movie=="":
        messagebox.showerror("Invalid Choice", "Please enter a valid movie name")
    else:
        colors = ["#E4DBBF"]
        #colors = ["cyan2", "SeaGreen2", "medium orchid", "burlywood1", "gray73", "gold"]
        list1 = get_list(movie)
        i=0
        for item in list1:
            Label(bottomFrame, text=item , fg="#383127", bg=random.choice(colors)).pack(side=TOP, fill=X)

root = Tk()
root.title("Movie Recommendation System")
topFrame = Frame(root)
topFrame.pack(fill=X)
label1 = Label(topFrame, text="Movie Recommendation System", fg="#DC5B21", bg="#E4DBBF")
label1.config(font=("Didot 24 bold"))
label1.pack(fill=X)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM, fill=X)
label2 = Label(root, text="Enter a movie of your choice:-  ")
entry1 = Entry(root, width=30)
button1 = Button(root, text="Get recommendations", command=getrec)


label2.pack(side=LEFT)
entry1.pack(side=LEFT)
button1.pack(side=BOTTOM)
root.mainloop()