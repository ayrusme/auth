"""
The models for the Project related to authentication
"""
from copy import deepcopy
from datetime import datetime, timedelta
from time import time

from flask_jwt_extended import create_access_token, create_refresh_token

from auth.auth_codes import EXPIRY_DURATION
from database.engine import SESSION, find_record
from database.schema import User, UserAuthentication
from helpers.codes import AUTH_OKAY, NOT_AUTHENTICATED


def login(username, password):
    """
    Model for the login controller

    Params
    ------------
    username: str
    password: str

    Returns
    ------------
    user.serialize: Model serializer in the schema
        Whatever information is available in the user object
    access_token: JWT access token
        The token using which authenticated calls can be made
    expires_in: timedelta
        The time in which the token will expire (in seconds)
    refresh_token: JWT refresh token
        The refresh token using which a new access token can be fetched
        JWT refresh tokens do not expire
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
        response['payload']['access_token'] = create_access_token(
            identity=user.guid,
            expires_delta=EXPIRY_DURATION
        )
        response['payload']['expires_in'] = EXPIRY_DURATION.seconds
        response['payload']['not_before'] = int(time() + EXPIRY_DURATION.seconds)
        response['payload']['refresh_token'] = create_refresh_token(
            identity=user.guid,
            expires_delta=False
        )
    return response
