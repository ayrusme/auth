"""
This file holds the authentication layer for all incoming requests
"""
from functools import wraps
from uuid import UUID

from flask import abort, jsonify, request
from flask_jwt_extended import get_jwt_claims, verify_jwt_in_request

from helpers.codes import TOKEN_ERROR, TROOPER_ROLE_ID, VADER_ROLE_ID

from .auth_codes import JWT_ALGORITHM, JWT_SECRET


def vader_wrapper(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """
        Auth wrapper for Astrix Backend

        Use this wrapper to make sure only admin can access certain routes
        """
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if str(UUID(VADER_ROLE_ID)) not in claims['roles']:
            return jsonify(msg='Admins only!'), 403
        else:
            return fn(*args, **kwargs)
    return wrapper


def trooper_wrapper(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """
        Auth wrapper for Astrix Backend

        Use this wrapper to make sure only admins and troopers have access
        """
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if VADER_ROLE_ID in claims['roles'] or TROOPER_ROLE_ID in claims['roles']:
            return fn(*args, **kwargs)
        else:
            return jsonify(msg='Admins only!'), 403
    return wrapper
