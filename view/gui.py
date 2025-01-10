from tkinter import *
from tkinter import messagebox

def displayRecommendations():
    for widget in bottomFrame.winfo_children():
        widget.destroy()
    
    movie = entry1.get()
    if not movie:
        messagebox.showerror("Invalid Choice", "Please enter a valid movie name")
        return

    recommended_movies = getList(movie, df)
    if not recommended_movies:
        return

    for item in recommended_movies:
        Label(bottomFrame, text=item, fg="#383127", bg="#E4DBBF").pack(side=TOP, fill=X)

def buildGUI():
    # Set up GUI
    root = Tk()
    root.title("Movie Recommendation System")

    topFrame = Frame(root)
    topFrame.pack(fill=X)
    Label(topFrame, text="Movie Recommendation System", fg="#000000", bg="#f5c518", font=("Roboto", 24, "bold")).pack(fill=X)

    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM, fill=X)

    Label(root, text="Enter a movie you like: ").pack(side=LEFT)
    entry1 = Entry(root, width=30)
    entry1.pack(side=LEFT)

    Button(root, text="Get recommendations", command=display_recommendations).pack(side=BOTTOM)

    root.mainloop()