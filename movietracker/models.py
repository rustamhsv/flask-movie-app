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

    def __init__(self, movie_id, title, poster, release_date, vote_average):
        self.movie_id = movie_id
        self.title = title
        self.poster = f"https://www.themoviedb.org/t/p/w1280{poster}"
        self.release_date = release_date
        self.vote_average = vote_average
