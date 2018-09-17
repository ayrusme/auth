"""
This file holds the authentication layer for all incoming requests
"""

from functools import wraps

import jwt
from sanic.exceptions import abort, HeaderNotFound

import app.auth.auth_codes as codes

"""
Authentication Wrapper for Project Astrix
"""


def auth_wrapper():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            if not "Authorization" in request.headers:
                abort(401)
            # TODO Extract jwt from header for user identity
            response = await f(request, *args, **kwargs)
            return response
        return decorated_function
    return decorator
