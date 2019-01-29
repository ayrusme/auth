"""
The models for the Project related to authentication
"""
from database.engine import SESSION, find_record
from flask_jwt_extended import create_access_token


def login(username, password):
    """
    Model for the login controller
    """
    result = False
    access_token = None
    refresh_token = None
    # TODO Link DB
    return result, access_token, refresh_token
