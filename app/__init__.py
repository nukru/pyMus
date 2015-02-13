from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail

from config import config

db = SQLAlchemy()
mail = Mail()

def create_app(config_name):
    ''' Setup Flask app '''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    mail.init_app(app)

    return app
