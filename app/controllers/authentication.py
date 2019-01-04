"""
The controllers for the authentication
"""

from copy import deepcopy

from flask import abort, jsonify, request
from flask.blueprints import Blueprint
from flask_jwt_extended import (create_access_token, get_jwt_identity,
                                jwt_refresh_token_required)

from helpers.codes import AUTH_OKAY, BAD_REQUEST

auth_blueprint = Blueprint(
    'authentication_v1', __name__, url_prefix='/v1/auth')


@auth_blueprint.route('/login', methods=['POST'])
def login(request):
    """
    Login Endpoint
    """
    if hasattr(request, "json") and request.json is not None:
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if username is not None and password is not None:
            # TODO Finish login flow. Construct JWT. Link Model.
            pass
    return jsonify(BAD_REQUEST)


@auth_blueprint.route('/register', methods=['POST'])
def signup(request):
    """
    Endpoint to allow users to signup
    """
    pass


@auth_blueprint.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh_token():
    """
    Route to provide the refresh token after the auth token expires
    """
    current_user = get_jwt_identity()
    if current_user == None:
        return abort(401)
    response = deepcopy(AUTH_OKAY)
    response['access_token'] = create_access_token(identity=current_user)
    return jsonify(response), 200
