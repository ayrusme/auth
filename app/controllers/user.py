from copy import deepcopy

from flask import abort
from flask import jsonify
from flask import request
from flask.blueprints import Blueprint
from flask_jwt_extended import create_access_token
from models.user import register_user

user_blueprint = Blueprint('user_routes', __name__, url_prefix='/v1/')


@user_blueprint.route('/create-user', methods=['POST'])
def signup():
    """
    Endpoint to allow users to signup
    """
    result = None
    if hasattr(request, "json") and request.json is not None:
        result = register_user(request.get_json())
    return result
