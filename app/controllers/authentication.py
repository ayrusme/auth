"""
The controllers for the authentication
"""

from flask.blueprints import Blueprint
from flask import jsonify

from helpers.codes import BAD_REQUEST

auth_blueprint = Blueprint('authentication_v1', __name__, url_prefix='/v1/auth')


@auth_blueprint.route('/login', methods=['POST'])
async def login(request):
    """
    Login Endpoint
    """
    if hasattr(request, "json") and request.json is not None:
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if username is not None and password is not None:
            # TODO Finish login flow. Construct JWT. Link Model.
            pass
        else:
            return jsonify(BAD_REQUEST['payload'], status=BAD_REQUEST['status_code'])
    else:
        return jsonify(BAD_REQUEST['payload'], status=BAD_REQUEST['status_code'])

@auth_blueprint.route('/register', methods=['POST'])
async def signup(request):
    """
    Endpoint to allow users to signup
    """
