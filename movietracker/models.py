class Movie:
    """ Define Movie objects """
    def __init__(self, movie_id, title, poster, release_date, vote_average):
        self.movie_id = movie_id
        self.title = title
        self.poster = f"https://www.themoviedb.org/t/p/w1280{poster}"
        self.release_date = release_date
        self.vote_average = vote_average


