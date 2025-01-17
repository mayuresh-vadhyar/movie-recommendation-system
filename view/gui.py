from tkinter import *
from tkinter import messagebox
from models import contentBasedFiltering

class GUI:
    def __init__(self):
        print('started')
        self.buildGUI()

    def displayRecommendations(self):
        cbf = contentBasedFiltering.contentBasedFiltering()
        for widget in self.bottomFrame.winfo_children():
            widget.destroy()
        
        movie = self.entry1.get()
        if not movie:
            messagebox.showerror("Invalid Choice", "Please enter a valid movie name")
            return

        recommended_movies = cbf.getList(movie)
        if not recommended_movies:
            return

        for item in recommended_movies:
            Label(self.bottomFrame, text=item, fg="#383127", bg="#E4DBBF").pack(side=TOP, fill=X)

    def buildGUI(self):
        # Set up GUI
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