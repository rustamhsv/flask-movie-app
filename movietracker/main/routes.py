from . import main
from flask import render_template, request, redirect, url_for
from ..request import get_movies
from .utils import save_data_to_db
from movietracker.models import MovieDB
from .forms import SearchForm


@main.route('/')
@main.route('/home')
def home():
    # get movies from API
    popular_movies = get_movies(pages=10)

    # save movies to database
    save_data_to_db(popular_movies)

    # paginate
    page = request.args.get('page', 1, type=int)

    # get movies from database
    popular_movies_from_db = MovieDB.query.paginate(page=page, per_page=24)

    return render_template('home.html', popular_movies=popular_movies_from_db)


@main.route('/movie/<movie_id>/<movie_title>')
def movie_page(movie_id, movie_title):
    movie = MovieDB.query.filter_by(movie_id=movie_id).first_or_404()
    return render_template('movie.html', movie=movie)


@main.route('/search', methods=['GET', 'POST'])
def search():
    text_to_search = request.form.get('search_text')
    print('TSEARCH:', text_to_search)

    # if text for search is not provided
    if not text_to_search:
        text_to_search = ''

    # paginate
    page = request.args.get('page', 1, type=int)

    # get movies from database
    search_results = MovieDB.query.filter(MovieDB.title.contains(text_to_search)).\
        paginate(page=page, per_page=24)

    return render_template('search.html', search_results=search_results)

