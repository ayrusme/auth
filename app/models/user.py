"""
This file contains the models for the user
"""
import uuid
from copy import deepcopy
from datetime import datetime

from database.engine import SESSION, find_record
from helpers.codes import BAD_REQUEST, MUGGLE, REGISTER_SUCCESS, ENTITY_EXISTS

from . import (AUTHENTICATION_SCHEMA_VALIDATOR, USER_SCHEMA_VALIDATOR, User,
               UserAuthentication, UserRole)


def register_user(user_details, role=MUGGLE):
    """
    Model for creating a new user
    """
    response = deepcopy(BAD_REQUEST)
    # Validate the incoming details
    if AUTHENTICATION_SCHEMA_VALIDATOR.is_valid(user_details):
        session = SESSION()
        # TODO Add check to see if user exists
        result, session = find_record(UserAuthentication, session, {
            "username": user_details['username']
        })
        session.flush()
        if not result:
            user_id = uuid.uuid4()
            # create user auth
            user_authentication = UserAuthentication(
                **{
                    "guid": uuid.uuid4(),
                    "user_id": user_id,
                    "created_at": datetime.now(),
                    "updated_at": datetime.now(),
                }, **user_details
            )
            # assign role
            user_role = UserRole(**{
                "guid": uuid.uuid4(),
                "user_id": user_id,
                "role_id": role['role_id']
            })
            # create user object
            user = User(**{
                "guid": user_id,
                "phone": user_details['username'],
                "authentication": [user_authentication],
                "role": [user_role]
            })
            session.add(user)
            session.commit()
            response = REGISTER_SUCCESS
        response = deepcopy(ENTITY_EXISTS)
    return response
