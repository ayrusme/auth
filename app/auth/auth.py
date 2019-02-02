"""
This file holds the authentication layer for all incoming requests
"""
from functools import wraps

from flask import abort, jsonify, request
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                get_jwt_identity, jwt_refresh_token_required,
                                jwt_required)

from auth_codes import JWT_ALGORITHM, JWT_SECRET
from helpers.codes import TOKEN_ERROR


def auth_wrapper(f):
    """
    Auth wrapper for Astrix Backend

    Use this wrapper to make sure only admin can access certain routes
    """
    @wraps(f)
    def wrapper(*args, **kws):
        if 'Authorization' not in request.headers:
            abort(401)

        user = None
        data = request.headers['Authorization'].encode('ascii', 'ignore')
        token = str.replace(str(data), 'Bearer ', '')
        try:
            user = get_jwt_identity()
        except BaseException:
            abort(401)
        return f(user, *args, **kws)
    return wrapper
