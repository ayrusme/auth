"""
The models for the Project related to authentication
"""
from copy import deepcopy

from flask_jwt_extended import create_access_token, create_refresh_token

from database.engine import SESSION, find_record
from database.schema import UserAuthentication
from helpers.codes import AUTH_OKAY, NOT_AUTHENTICATED


def login(username, password):
    """
    Model for the login controller
    """
    result = deepcopy(NOT_AUTHENTICATED)
    session = SESSION()
    response, session = find_record(UserAuthentication, session, {"username": username})
    session.flush()
    if response and response.password == password:
        result = deepcopy(AUTH_OKAY)
        result['payload']['access_token'] = create_access_token(identity=username)
        result['payload']['refresh_token'] = create_refresh_token(identity=username)
    return result
