from tkinter import *
from tkinter import messagebox
from models.DataFrame import DataFrame
from models.ContentBasedFiltering import ContentBasedFiltering
from models.CustomException import CustomException
from constants import ERRORS as errors
from constants import GUI as constants

class GUI:
    def __init__(self):
        self.buildGUI()
        print('started')

    def displayRecommendations(self):
        try:
            cbf = ContentBasedFiltering()
            for widget in self.bottomFrame.winfo_children():
                widget.destroy()
            
            movie = self.entry1.get()
            if not movie:
                raise CustomException(errors.MOVIE_NOT_FOUND)
            
            movieIndex = DataFrame().getIndexOfClosestTitle(movie)
            recommended_movies = cbf.getRecommendedMovies(movieIndex)
            if not recommended_movies:
                raise CustomException(errors.NO_SIMILAR_MOVIES)

            for item in recommended_movies:
                Label(self.bottomFrame, text=item, fg=constants.MOVIE_ITEM_FG, bg=constants.MOVIE_ITEM_BG).pack(side=TOP, fill=X)
        except CustomException as E:
            if (E.message == errors.MOVIE_NOT_FOUND):
                messagebox.showerror("Movie does not exist", "No such movie exists. Please enter a valid movie name.")
            elif (E.message == errors.NO_SIMILAR_MOVIES):
                messagebox.showerror("No similar movies", "Please try another movie")
            else:
                messagebox.showerror(E.error_code, E.message)


    def buildGUI(self):
        root = Tk()
        root.title("Movie Recommendation System")

        topFrame = Frame(root)
        topFrame.pack(fill=X)
        Label(topFrame, text="Movie Recommendation System", fg=constants.TITLE_FG, bg=constants.TITLE_BG, font=constants.TITLE_FONT).pack(fill=X)

        self.bottomFrame = Frame(root)
        self.bottomFrame.pack(side=BOTTOM, fill=X)

        Label(root, text="Enter a movie you like: ").pack(side=LEFT)
        self.entry1 = Entry(root, width=30)
        self.entry1.pack(side=LEFT)

        Button(root, text="Get recommendations", command=self.displayRecommendations).pack(side=BOTTOM)

        root.mainloop()