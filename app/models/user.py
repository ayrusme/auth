"""
This file contains the models for the user
"""
import uuid
from datetime import datetime

from helpers.codes import MUGGLE

from . import AUTHENTICATION_SCHEMA_VALIDATOR
from . import Role
from . import User
from . import USER_SCHEMA_VALIDATOR
from . import UserAuthentication
from . import UserRole


def register_user(user_details):
    """
    Model for creating a new user
    """
    result = None
    # Validate the incoming details
    if AUTHENTICATION_SCHEMA_VALIDATOR.is_valid(user_details):
        # register user with just the username and password
        user_authentication = UserAuthentication(
            **{
                "guid": uuid.uuid4(),
                "user_id": uuid.uuid4(),
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            }, **user_details
        )
        # assign role as muggle
        user_role = Role(**MUGGLE)
    return result
