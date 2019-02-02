"""
This file contains the models for the user
"""
import uuid
from copy import deepcopy
from datetime import datetime

from database.engine import SESSION, find_record
from helpers.codes import (BAD_REQUEST, ENTITY_EXISTS, MUGGLE, NOT_FOUND,
                           REGISTER_SUCCESS, RECORD_FOUND)

from . import (AUTHENTICATION_SCHEMA_VALIDATOR, USER_SCHEMA_VALIDATOR,
               USER_UPDATE_VALIDATOR, User, UserAuthentication, UserRole)


def register_user(user_details, role=MUGGLE):
    """
    Model for creating a new user

    Params
    ---------------
    user_details: dict
        The details of the user, enough to pass the AUTH SCHEMA
    role: dict
        An optional parameter defining the role of the user
    """
    response = deepcopy(BAD_REQUEST)
    # Validate the incoming details
    if AUTHENTICATION_SCHEMA_VALIDATOR.is_valid(user_details):
        session = SESSION()
        result, session = find_record(UserAuthentication, session, {
            "username": user_details['username']
        })
        if not result:
            user_id = uuid.uuid4().hex
            # create user auth
            user_authentication = UserAuthentication(
                **{
                    "guid": uuid.uuid4().hex,
                    "user_id": user_id,
                    "created_at": datetime.now(),
                    "updated_at": datetime.now(),
                }, **user_details
            )
            # assign role
            user_role = UserRole(**{
                "guid": uuid.uuid4().hex,
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
            response = deepcopy(REGISTER_SUCCESS)
        else:
            response = deepcopy(ENTITY_EXISTS)
        session.close()
    return response


def get_user(user_details):
    """
    Function to get a user from a DB

    Returns
    --------------
    Either the user object or no record exists dict
    """
    response = deepcopy(NOT_FOUND)
    if USER_UPDATE_VALIDATOR.is_valid(user_details):
        session = SESSION()
        result, session = find_record(User, session, user_details)
        if result:
            response = deepcopy(RECORD_FOUND)
            response['payload'] = result.serialize
        session.close()
    return response


def modify_user(user_details):
    """
    Function to modify the user details for a particular user

    Params
    --------------
    Returns
    --------------
    """
