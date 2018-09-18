"""
The controllers for the authentication
"""

from sanic.blueprints import Blueprint
from sanic.response import json

from app.helpers.codes import BAD_REQUEST

auth_blueprint = Blueprint('authentication_v1', url_prefix='/auth')


@auth_blueprint.route('/login', methods=['POST'])
async def login(request):
    """Login Endpoint
    """
    if hasattr(request, "json") and request.json is not None:
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if username is not None and password is not None:
            # TODO Finish login flow. Construct JWT. Link Model.
            pass
        else:
            return json(BAD_REQUEST['payload'], status=BAD_REQUEST['status_code'])
    else:
        return json(BAD_REQUEST['payload'], status=BAD_REQUEST['status_code'])
