import pickle
import streamlit as st  # type: ignore
import requests

# Function to fetch the movie poster using the movie's ID
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=6be1bffe6b6e31e1816a73ddcfb4ef0b".format(movie_id)
    data = requests.get(url).json()
    
    # Check if the 'poster_path' key exists in the response
    poster_path = data.get('poster_path')
    
    if poster_path:
        full_path = "http://image.tmdb.org/t/p/w185/" + poster_path
        return full_path
    else:
        return "https://via.placeholder.com/185"  # Return placeholder image if no poster

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movies_name = []
    recommended_movies_poster = []
    
    for i in distances[1:6]:  # Get the top 5 recommendations
        movie_id = movies.iloc[i[0]]['movie_id']  # Get the movie_id for the recommended movie
        recommended_movies_poster.append(fetch_poster(movie_id))  # Fetch poster using the movie_id
        recommended_movies_name.append(movies.iloc[i[0]]['title'])  # Append the movie title
    
    return recommended_movies_name, recommended_movies_poster

# Streamlit app setup
st.header("Movies Recommendation System")

# Load movies and similarity data from pickle files
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

# Select a movie from the dropdown
movie_list = movies['title'].values
selected_movie = st.selectbox('Type movie name', movie_list)

# Show recommendations when the button is clicked
if st.button('Show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    
    # Display the recommendations in 5 columns
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])

    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])

    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])

    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])
