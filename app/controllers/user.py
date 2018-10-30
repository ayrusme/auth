from flask import jsonify

from flask.blueprints import Blueprint

user_blueprint = Blueprint('user_routes', __name__, url_prefix='/v1/')
