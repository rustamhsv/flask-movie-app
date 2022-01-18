from flask import Flask
from movietracker.config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap()  # initialize Bootstrap
db = SQLAlchemy()  # initialize SQLAlchemy Database
login_manager = LoginManager()  # initialize Login Manager


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # initalize flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # register main Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # register users Blueprint
    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)

    return app



