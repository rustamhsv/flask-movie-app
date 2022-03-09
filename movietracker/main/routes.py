from flask_login import current_user

from . import main
from flask import render_template, request, redirect, url_for, flash
from datetime import datetime
from .. import db
from ..request import get_movies
from .utils import save_data_to_db
from movietracker.models import MovieDB, Review
from .forms import SearchForm, ReviewForm


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


@main.route('/movie/<movie_id>/<movie_title>', methods=['GET', 'POST'])
def movie_page(movie_id, movie_title):
    movie = MovieDB.query.filter_by(movie_id=movie_id).first_or_404()

    form = ReviewForm()
    if current_user.is_authenticated:
        if form.validate_on_submit():
            current_date_time = datetime.now().replace(second=0, microsecond=0)
            # a = current_date_time.strftime('%Y-%m-%d %H:%M')
            review = Review(date_posted=current_date_time, content=form.review.data,
                            author=current_user.username, movie_id=movie.movie_id)

            # add users to database session
            db.session.add(review)

            # commit users
            db.session.commit()

            flash('Review posted!', category='alert alert-success')
            return redirect(url_for('main.movie_page', movie_id=movie.movie_id, movie_title=movie.title))

    reviews = Review.query.filter_by(movie=movie)
    return render_template('movie.html', movie=movie, reviews=reviews, form=form)


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


# @main.route('/movie/<movie_id>/<movie_title>')
# def write_review(movie_id):
#     movie = MovieDB.query.filter_by(movie_id=movie_id).first_or_404()
#     reviews = MovieDB.query.filter_by(movie_id=movie_id)
#     return render_template('movie.html', movie=movie)

