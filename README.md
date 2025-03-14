# Movie Recommendation System

This is a **Movie Recommendation System** built using **Python**. It allows users to input a movie name and receive recommendations for similar movies based on various features like keywords, cast, genres, and director. The recommendation engine is powered by **cosine similarity** using features extracted through the **CountVectorizer** from the movie dataset. A **Tkinter** GUI is available for a user-friendly interface, and a **Flask-based REST API server** is included for programmatic access.

## Features
- Displays top **20 recommended movies** (configurable in `constants.py`) based on user input.
- Cosine similarity-based recommendation engine.
- **Configurable features** to be used for recommendations.
- Fuzzy matching to handle movie title variations (e.g., "titanoc" matches "Titanic").
- User-friendly GUI for entering a movie name and viewing recommendations.
- **Flask-based REST API** for serving recommendations.
- **GUI localization support** using `en_us.json` (configurable in `constants.py`).
- **Customizable dataset file** (configurable in `constants.py`).
- **Pagination support** for API recommendations.

## Requirements

The following Python libraries are required to run the system:

- `pandas`
- `numpy`
- `scikit-learn`
- `fuzzywuzzy`
- `python-Levenshtein`
- `tkinter`
- `Flask`

You can install the required libraries by running:

```bash
pip install pandas numpy scikit-learn fuzzywuzzy python-Levenshtein Flask
```

Note: `Tkinter` comes pre-installed with Python, so no need to install it separately.

## Setup and Usage

### GUI Mode

1. **Clone the repository** or download the script to your local machine.

    ```bash
    git clone https://github.com/mayuresh-vadhyar/movie-recommendation-system.git
    ```

2. **Download the movie dataset** (`movie_dataset.csv`) and place it in the same directory as the script. The dataset's column names and the features used for cosine similarity evaluation are configurable. Ensure the dataset structure aligns with your configuration settings.

3. **Run the Python script** to start the GUI application:

    ```bash
    python main.py
    ```

4. **Enter a movie title** in the input field and click the "Get recommendations" button. The system will display a list of similar movies based on the entered movie.

### API Mode (Flask Server)

1. **Run the Flask API server**:

    ```bash
    python server.py
    ```

2. **Available API Endpoints**:

    - `GET /movies/index?title=<movie_title>` → Returns the index of a movie by title.
    - `GET /movies/closest-index?title=<movie_title>` → Returns the index of the closest matching title.
    - `GET /movies/recommendations/<movieIndex>` → Returns movie recommendations based on the movie index.
    - `GET /movies/recommendations?title=<movie_title>&page=<page_number>&size=<page_size>` → Returns paginated movie recommendations based on closest matching movie title.

### Configurations

All configurations can be modified in constants.py:

1. Dataset Configuration: The dataset file and the columns used for recommendations are configurable.

2. Feature Selection: You can define which features (e.g., keywords, cast, genres, director) should be used for similarity calculations.

3. Number of Recommendations: The number of movies returned can be configured based on user preference.

4. Pagination: API recommendations support pagination with configurable page size.

5. Minimum Threshold for Title Matching: The fuzzy matching threshold for movie title similarity can be adjusted.

6. Default Number of Recommendations: The default count of recommendations to return is configurable.

7. Localization:

    - GUI strings are stored in the en_us.json file for localization.

    - You can customize the localization by changing the file name in constants.py and creating a new JSON file with the desired translations.

## How It Works
1. The system reads the movie dataset and combines key features into a single feature vector for each movie.
2. The combined features are processed using **CountVectorizer**, which converts text data into a matrix of token counts.
3. **Cosine similarity** is calculated between the movie the user inputs and every other movie in the dataset.
4. The top N movies (configurable) with the highest similarity scores are recommended and displayed in the GUI or served via the API.

## Future Improvements
- Allow the user to filter recommendations by genre or year.
- Add more features (e.g., movie ratings or runtime) to improve recommendation accuracy.
- Implement machine learning models to improve similarity calculation.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
