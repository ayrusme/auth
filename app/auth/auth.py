"""
This file holds the authentication layer for all incoming requests
"""

from functools import wraps

from flask import abort, request, jsonify

from auth.auth_codes import JWT_ALGORITHM, JWT_SECRET
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                get_jwt_identity, jwt_refresh_token_required,
                                jwt_required)


def encrypt(payload):
    """
    Function to encrypt the given payload
    """
    """
    Auth wrapper for Astrix Backend
    """
    # TODO Add encryption technique
    pass


def decrypt(payload):
    """
    Function to decrypt the given payload
    """
    # TODO Add decryption technique
    pass


def auth_wrapper(f):
    """
    Auth wrapper for Astrix Backend
    
    Use this wrapper to make sure only admin can access certain routes
    """
    @wraps(f)
    def wrapper(*args, **kws):
        if not 'Authorization' in request.headers:
            abort(401)

        user = None
        data = request.headers['Authorization'].encode('ascii', 'ignore')
        token = str.replace(str(data), 'Bearer ', '')
        try:
            user = get_jwt_identity()
        except:
            abort(401)
        return f(user, *args, **kws)
    return wrapper
