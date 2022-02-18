import requests
from .models import Movie
from movietracker.config import Config


def get_movies(pages=2):

    # get API key
    config = Config()
    api_key = config.TMDB_API_KEY

    all_movies = []
    for page in range(1, pages):
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US' \
              f'&sort_by=popularity.desc&include_adult=false&include_video=false&page={page}' \
              f'&with_watch_monetization_types=flatrate'
        print(url)

        # get json response
        response = requests.get(url)
        json_data = response.json()

        # get movies list
        movies = json_data['results']
        all_movies += movies

    movie_objects = process_results(all_movies)

    return movie_objects


def process_results(movies):
    """ process json response and return list of Movie objects """

    movie_objects = []

    # iterate through movies
    for movie in movies:
        movie_id = movie.get('id')
        title = movie.get('title')
        poster = movie.get('poster_path')
        release_date = movie.get('release_date')
        vote_average = movie.get('vote_average')
        vote_count = movie.get('vote_count')
        overview = movie.get('overview')

        if poster:
            movie_object = Movie(movie_id, title, poster, release_date, vote_average, vote_count, overview)
            movie_objects.append(movie_object)

    return movie_objects
