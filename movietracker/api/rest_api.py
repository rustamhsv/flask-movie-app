from flask import Blueprint, jsonify, abort, g
from werkzeug.security import check_password_hash

from movietracker import auth
from movietracker.models import User, MovieDB

api = Blueprint('api', __name__)


# API for accessing MovieTracker services
@api.route('/api/v1/movies', methods=['GET'])
@auth.login_required
def get_movies_api():
    movies = MovieDB.query.all()
    if not movies:
        abort(404)

    movie_list = []
    for movie in movies:
        movie_dict = {'movie_id:': movie.movie_id, 'title': movie.title,
                      'year': movie.release_date, 'rating': movie.vote_average,
                      'about': movie.overview}
        movie_list.append(movie_dict)

    return jsonify({'movies': movie_list})


@api.route('/api/v1/movies/<int:movie_id>', methods=['GET'])
@auth.login_required
def get_movie_api(movie_id):
    movie = MovieDB.query.filter_by(movie_id=movie_id).first()
    if not movie:
        abort(404)
    movie_dict = {'movie_id:': movie.movie_id, 'title': movie.title,
                  'year': movie.release_date, 'rating': movie.vote_average,
                  'about': movie.overview}

    return jsonify({'movie': movie_dict})


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return False
    g.user = user
    return True