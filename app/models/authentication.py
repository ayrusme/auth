"""
The models for the Project related to authentication
"""
from copy import deepcopy

from flask_jwt_extended import create_access_token, create_refresh_token

from database.engine import SESSION, find_record
from database.schema import UserAuthentication, User
from helpers.codes import AUTH_OKAY, NOT_AUTHENTICATED


def login(username, password):
    """
    Model for the login controller
    """
    response = deepcopy(NOT_AUTHENTICATED)
    session = SESSION()
    # result, session = find_record(UserAuthentication, session, {"username": username})
    user, auth = session.query(User, UserAuthentication).filter(
        UserAuthentication.username == username
        ).first()
    session.flush()
    if user and auth and auth.password == password:
        response = deepcopy(AUTH_OKAY)
        response['payload']['user'] = user.serialize
        response['payload']['access_token'] = create_access_token(identity=user.guid)
        response['payload']['refresh_token'] = create_refresh_token(identity=user.guid)
    return response
