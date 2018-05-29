# third-party imports
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local imports
from instance.config import app_config

# instantiating the db
db = SQLAlchemy()

def create_app(config_name):
    """Instantiating the app and its configurations"""
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")

    db.init_app(app)

    return app