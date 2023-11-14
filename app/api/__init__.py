from flask import Blueprint

api_blueprint = Blueprint('api', __name__)

from .users import user_blueprint

api_blueprint.register_blueprint(user_blueprint, url_prefix='/users')

from .user_data import user_data_blueprint

api_blueprint.register_blueprint(user_data_blueprint, url_prefix='user_data')
