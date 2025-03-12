from tkinter import *
from tkinter import messagebox
from models.DataFrame import DataFrame
from models.ContentBasedFiltering import ContentBasedFiltering
from models.CustomException import CustomException
from view.Translator import getString
from constants import ERRORS as errors
from constants import GUI as constants

class GUI:
    def __init__(self):
        print('started')
        self.buildGUI()

    def displayRecommendations(self):
        try:
            cbf = ContentBasedFiltering()
            for widget in self.bottomFrame.winfo_children():
                widget.destroy()
            
            movie = self.entry1.get()
            if not movie:
                raise CustomException(errors.MOVIE_NOT_FOUND, 404)
            
            movieIndex = DataFrame().getIndexOfClosestTitle(movie)
            recommended_movies = cbf.getRecommendedMovies(movieIndex)
            if not recommended_movies:
                raise CustomException(errors.NO_SIMILAR_MOVIES)

            for item in recommended_movies:
                Label(self.bottomFrame, text=item, fg=constants.MOVIE_ITEM_FG, bg=constants.MOVIE_ITEM_BG).pack(side=TOP, fill=X)
        except CustomException as E:
            if (E.message == errors.MOVIE_NOT_FOUND):
                messagebox.showerror(getString('MOVIE_NOT_FOUND_TITLE'), getString('MOVIE_NOT_FOUND_MESSAGE'))
            elif (E.message == errors.NO_SIMILAR_MOVIES):
                messagebox.showerror(getString('NO_SIMILAR_MOVIES_TITLE'), getString('NO_SIMILAR_MOVIES_MESSAGE'))
            if (E.message == errors.INVALID_INDEX):
                messagebox.showerror(getString('INVALID_INDEX_TITLE'), getString('INVALID_INDEX_MESSAGE'))
            else:
                messagebox.showerror(E.error_code, E.message)


    def buildGUI(self):
        root = Tk()
        root.title(getString('windowTitle'))

        topFrame = Frame(root)
        topFrame.pack(fill=X)
        Label(topFrame, text=getString('windowTitle'), fg=constants.TITLE_FG, bg=constants.TITLE_BG, font=constants.TITLE_FONT).pack(fill=X)

        self.bottomFrame = Frame(root)
        self.bottomFrame.pack(side=BOTTOM, fill=X)

        Label(root, text=getString('movieNamePrompt')).pack(side=LEFT)
        self.entry1 = Entry(root, width=30)
        self.entry1.pack(side=LEFT)

        Button(root, text=getString('submitButton'), command=self.displayRecommendations).pack(side=BOTTOM)

        root.mainloop()