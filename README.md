# Movie Recommendation System

This is a **Movie Recommendation System** built using **Python**. It allows users to input a movie name and receive recommendations for similar movies based on various features like keywords, cast, genres, and director. The recommendation engine is powered by **cosine similarity** using features extracted through the **CountVectorizer** from the movie dataset. A **Tkinter** GUI is used for a user-friendly interface.

## Features
- Fuzzy matching to handle movie title variations (e.g., "titanic" matches "Titanic").
- Cosine similarity-based recommendation engine.
- User-friendly GUI for entering a movie name and viewing recommendations.
- Displays top 20 recommended movies based on user input.

## Requirements

The following Python libraries are required to run the system:

- `pandas`
- `numpy`
- `scikit-learn`
- `fuzzywuzzy`
- `python-Levenshtein`
- `tkinter`

You can install the required libraries by running:

```bash
pip install pandas numpy scikit-learn fuzzywuzzy python-Levenshtein
```

Note: `Tkinter` comes pre-installed with Python, so no need to install it separately.

## Setup and Usage

1. **Clone the repository** or download the script to your local machine.

    ```bash
    git clone https://github.com/mayuresh-vadhyar/movie-recommendation-system.git
    ```

2. **Download the movie dataset** (`movie_dataset.csv`) and place it in the same directory as the script. The dataset should have the following columns:
    - `index`: A unique identifier for each movie.
    - `title`: The title of the movie.
    - `keywords`: Keywords describing the movie.
    - `cast`: Main cast of the movie.
    - `genres`: Genres the movie falls under.
    - `director`: Director of the movie.

3. **Run the Python script** to start the application:

    ```bash
    python movie_recommendation_system.py
    ```

4. **Enter a movie title** in the input field, and click the "Get recommendations" button. The system will display a list of similar movies based on the entered movie.

## Fuzzy Matching
The system uses **fuzzy matching** to handle variations in movie titles. For example:
- Entering "titanic" will match "Titanic".
- Entering "New Moon" will match "The Twilight Saga: New Moon".

The system uses a similarity threshold of 70% to find the closest matching title.

## How It Works
1. The system reads the movie dataset and combines key features (`keywords`, `cast`, `genres`, `director`) into a single feature vector for each movie.
2. The combined features are processed using **CountVectorizer**, which converts text data into a matrix of token counts.
3. **Cosine similarity** is calculated between the movie the user inputs and every other movie in the dataset.
4. The top 20 movies with the highest similarity scores are recommended and displayed in the GUI.


## Future Improvements
- Allow the user to filter recommendations by genre or year.
- Add more features (e.g., movie ratings or runtime) to improve recommendation accuracy.
- Implement machine learning models to improve similarity calculation.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to replace placeholders like the repository link or screenshot paths with actual values based on your project setup.
