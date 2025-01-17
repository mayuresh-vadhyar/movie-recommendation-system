from tkinter import *
from tkinter import messagebox
from models import contentBasedFiltering
from models.CustomException import CustomException

class GUI:
    def __init__(self):
        print('started')
        self.buildGUI()

    def displayRecommendations(self):
        try:
            cbf = contentBasedFiltering.ContentBasedFiltering()
            for widget in self.bottomFrame.winfo_children():
                widget.destroy()
            
            movie = self.entry1.get()
            if not movie:
                raise CustomException("MOVIE_NOT_FOUND")
            
            movieIndex = cbf.getIndexFromTitle(movie)
            recommended_movies = cbf.getRecommendedMovies(movieIndex)
            if not recommended_movies:
                raise CustomException("NO_SIMILAR_MOVIES")

            for item in recommended_movies:
                Label(self.bottomFrame, text=item, fg="#383127", bg="#E4DBBF").pack(side=TOP, fill=X)
        except CustomException as E:
            if (E.message == "MOVIE_NOT_FOUND"):
                messagebox.showerror("Movie does not exist", "No such movie exists. Please enter a valid movie name.")
            elif (E.message == "NO_SIMILAR_MOVIES"):
                messagebox.showerror("No similar movies", "Please try another movie")
            else:
                messagebox.showerror(E.error_code, E.message)


    def buildGUI(self):
        root = Tk()
        root.title("Movie Recommendation System")

        topFrame = Frame(root)
        topFrame.pack(fill=X)
        Label(topFrame, text="Movie Recommendation System", fg="#000000", bg="#f5c518", font=("Roboto", 24, "bold")).pack(fill=X)

        self.bottomFrame = Frame(root)
        self.bottomFrame.pack(side=BOTTOM, fill=X)

        Label(root, text="Enter a movie you like: ").pack(side=LEFT)
        self.entry1 = Entry(root, width=30)
        self.entry1.pack(side=LEFT)

        Button(root, text="Get recommendations", command=self.displayRecommendations).pack(side=BOTTOM)

        root.mainloop()