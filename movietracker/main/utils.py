from movietracker.models import MovieDB
from movietracker import db


def save_data_to_db(popular_movies):

    for movie in popular_movies:
        # add only new movies to db
        if MovieDB.query.filter(MovieDB.movie_id == movie.movie_id).first():
            continue

        movie_db = MovieDB(movie_id=movie.movie_id, title=movie.title, poster=movie.poster,
                           release_date=movie.release_date, vote_average=movie.vote_average,
                           vote_count=movie.vote_count, overview=movie.overview)

        db.session.add(movie_db)
        db.session.commit()
