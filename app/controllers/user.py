from copy import deepcopy

from flask import abort, jsonify, request
from flask.blueprints import Blueprint
from flask_jwt_extended import create_access_token

from models.user import register_user
from helpers.codes import BAD_REQUEST

USER_BLUEPRINT = Blueprint('user_routes_v1', __name__, url_prefix='/v1/')


@USER_BLUEPRINT.route('/create-user', methods=['POST'])
def signup():
    """
    Endpoint to allow users to signup
    """
    result = BAD_REQUEST
    if hasattr(request, "json") and request.json is not None:
        result = register_user(request.get_json())
    return jsonify(result['payload']), result['status_code']
