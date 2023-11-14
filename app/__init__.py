import os

from flask import Flask
from flask_jwt_extended import JWTManager
from .utils.database import db
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    secret_key = os.environ.get('JWT_SECRET_KEY')
    app.config['JWT_SECRET_KEY'] = secret_key

    jwt = JWTManager(app)

    db.init_app(app)

    from .api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
