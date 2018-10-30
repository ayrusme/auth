"""
This file holds the authentication layer for all incoming requests
"""

from functools import wraps

import jwt
from flask import abort, request

from auth.auth_codes import JWT_ALGORITHM, JWT_SECRET


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
    """
    @wraps(f)
    def wrapper(*args, **kws):
            if not 'Authorization' in request.headers:
               abort(401)

            user = None
            data = request.headers['Authorization'].encode('ascii','ignore')
            token = str.replace(str(data), 'Bearer ','')
            try:
                user = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])['sub']
            except:
                abort(401)

            return f(user, *args, **kws)            
    return wrapper