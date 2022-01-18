import os


class Config:
    """ Class for configuration of APP settings """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
