"""
This file contains the models for the user
"""
import uuid
from copy import deepcopy
from datetime import datetime

from database.engine import SESSION, find_record
from helpers.codes import (BAD_REQUEST, ENTITY_EXISTS, EXCEPTION_RES,
                           GENERIC_SUCCESS, NOT_FOUND, REBEL, RECORD_FOUND,
                           REGISTER_SUCCESS)

from . import (ADDRESS_SCHEMA_VALIDATOR, AUTHENTICATION_SCHEMA_VALIDATOR,
               USER_SCHEMA_VALIDATOR, USER_UPDATE_VALIDATOR, Address, User,
               UserAuthentication, UserRole)

# CREATE


def register_user(user_details, role=REBEL):
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
        try:
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
        except Exception as exp:
            session.rollback()
            response = deepcopy(EXCEPTION_RES)
            response['payload']['description'] = repr(exp)
        session.close()
    return response


def add_address(user_id, address):
    """
    Function to add address to the given userID
    """
    response = deepcopy(BAD_REQUEST)
    if ADDRESS_SCHEMA_VALIDATOR.is_valid(address):
        address = ADDRESS_SCHEMA_VALIDATOR.validate(address)
        address['guid'] = uuid.uuid4().hex
        address['user_id'] = user_id
        session = SESSION()
        try:
            address = Address(**address)
            session.add(address)
            session.commit()
            response = deepcopy(GENERIC_SUCCESS)
        except Exception as exp:
            session.rollback()
            response = deepcopy(EXCEPTION_RES)
            response['payload']['description'] = repr(exp)
        session.close()
    return response

# READ


def get_roles(user_id):
    """
    Function to get all the roles of the given user_id
    """
    session = SESSION()
    result = []
    try:
        user_roles, session = find_record(UserRole, session, {
            "user_id": user_id
        }, False)
        result = [role.role_id for role in user_roles]
    except Exception as exp:
        print(exp)
        session.rollback()
    session.close()
    return result


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
        try:
            result, session = find_record(User, session, user_details)
            if result:
                response = deepcopy(RECORD_FOUND)
                response['payload'] = result.serialize
        except Exception as exp:
            session.rollback()
            response = deepcopy(EXCEPTION_RES)
            response['payload']['description'] = repr(exp)
        session.close()
    return response

# MODIFY


def modify_user(user_id, user_details):
    """
    Function to modify the user details for a particular user

    Params
    --------------
    user_details: dict
        The details of the user that needs to be updated

    Returns
    --------------
    NOT_FOUND: dict
        If the user is not found

    """
    pass
