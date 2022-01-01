import requests
from .models import Movie
from movietracker.config import Config


def get_movies():

    # get API key
    config = Config()
    api_key = config.TMDB_API_KEY

    url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US' \
          '&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types' \
          '=flatrate'

    # get json response
    response = requests.get(url)
    json_data = response.json()

    # get movies list
    movies = json_data['results']
    movie_objects = process_results(movies)

    return movie_objects


def process_results(movies):
    """ process json response and return list of Movie objects """

    movie_objects = []
    for movie in movies:
        movie_id = movie.get('id')
        title = movie.get('title')
        poster = movie.get('poster_path')
        release_date = movie.get('release_date')
        vote_average = movie.get('vote_average')

        if poster:
            movie_object = Movie(movie_id, title, poster, release_date, vote_average)
            movie_objects.append(movie_object)

    return movie_objects
