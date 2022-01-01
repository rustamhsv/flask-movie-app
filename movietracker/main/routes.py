from . import main
from flask import render_template
from ..request import get_movies


@main.route('/')
@main.route('/home')
def home():
    popular_movies = get_movies()
    return render_template('home.html', popular_movies=popular_movies)
