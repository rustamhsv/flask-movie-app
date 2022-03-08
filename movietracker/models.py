import datetime

from movietracker import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user):
    return User.query.get(user)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    photo_file = db.Column(db.String(20), default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # reviews = db.relationship('Review', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.photo_file}')"


class Movie:
    """ Define Movie objects """

    def __init__(self, movie_id, title, poster, release_date, vote_average, vote_count, overview):
        self.movie_id = movie_id
        self.title = title
        self.poster = f"https://www.themoviedb.org/t/p/w1280{poster}"
        self.release_date = str(release_date)[:4]
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.overview = overview


class MovieDB(db.Model, UserMixin):
    movie_id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    poster = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.String(20))
    vote_average = db.Column(db.String(20), nullable=False)
    vote_count = db.Column(db.Integer)
    overview = db.Column(db.String)

    reviews = db.relationship('Review', backref='movie', lazy=True)


class Review(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String)
    movie_id = db.Column(db.Integer, db.ForeignKey('movieDB.movie_id'), nullable=True)
