
# Movie Recommender System

This project implements a Movie Recommender System using Python. It processes datasets containing movie details and metadata to generate recommendations based on genres, keywords, cast, and directors.
[Movie Recommender System](https://movierecosys9.streamlit.app/)

## Files

**Movie_Recommender_System.ipynb:**
The main Jupyter notebook containing the code for the Movie Recommender System.

**data/tmdb_5000_movies.csv:**
A dataset containing information about movies, including genres, keywords, revenue, and release dates.

**data/tmdb_5000_credits.csv:**
A dataset containing information about the cast and crew for each movie.


## Requirements

Make sure you have the following Python libraries installed:

```bash
  pip install numpy pandas matplotlib
```

## Features

- **Data Loading:** Loads movie and credit datasets.
- **Data Cleaning:** Removes null values and drops unnecessary columns.
- **Data Merging:** Merges movie and credit data based on the movie title.
- **Feature Extraction:** Extracts relevant features like genres, keywords, cast, and directors.
- **Data Transformation:** Transforms JSON-like columns into lists for further use.

## Usage

1. **Clone the repository and navigate to the project directory:**

```bash
git clone https://github.com/azadsingh3/Movie-Recommender-System.git
cd Movie_Recommender_System
```

2. Place the **datasets** (```tmdb_5000_movies.csv``` and ``` tmdb_5000_credits.csv```) inside the ```data``` folder.

3. **Run the Jupyter notebook:**

```bash
jupyter notebook Movie_Recommender_System.ipynb
```

4. **Try the Live App:**

Explore the deployed version of the Movie Recommender System here:

```bash
https://movierecosys9.streamlit.app/
```

## Code Structure

1. **Data Importing**

```bash
movies = pd.read_csv('data/tmdb_5000_movies.csv')
credits = pd.read_csv('data/tmdb_5000_credits.csv')
```

2. **Merging Datasets**

```bash
movies = movies.merge(credits, on='title')
```

3. **Data Cleaning**

```bash
movies.dropna(inplace=True)
```

4. **Feature Extraction**

```bash
def convert(text):
    return [i['name'] for i in ast.literal_eval(text)]
movies['genres'] = movies['genres'].apply(convert)
```

5. **Director Extraction**

```bash
def fetch_director(text):
    return [i['name'] for i in ast.literal_eval(text) if i['job'] == 'Director']
movies['crew'] = movies['crew'].apply(fetch_director)
```

## Output Example

Here is an example of the processed movie data:
|movie_id |title                   |genres               |cast         |crew       |
|---------|------|---------------------|-----|-----|
|19995    |Avatar                  |[Action, Adventure,.]|[Sam Worthington, ...]|[James Cameron]  |
|285      |Pirates of the Caribbean|[Adventure, Fantasy,.]  |[Johnny Depp, ...]    |[Gore Verbinski]|

## Contributing

Feel free to fork the project, submit issues, and send pull requests!

## License

This project is licensed under the MIT License.


## Acknowledgements

 - **TMDb** for providing the movie datasets.
 - **Pandas** and **Matplotlib** for data manipulation and visualization tools.
 

