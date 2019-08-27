"""
This file contains the models for the user
"""
import uuid
from copy import deepcopy
from datetime import datetime

from database.engine import SESSION, find_record
from helpers.codes import (BAD_REQUEST, ENTITY_EXISTS, EXCEPTION_RES,
                           GENERIC_SUCCESS, NOT_FOUND, RECORD_FOUND,
                           REGISTER_SUCCESS)
from models.roles import ALL_ROLES

from . import (ADDRESS_SCHEMA_VALIDATOR, AUTHENTICATION_SCHEMA_VALIDATOR,
               USER_SCHEMA_VALIDATOR, USER_UPDATE_VALIDATOR, Address, User,
               UserAuthentication)

# CREATE


def register_user(user_details):
    """
    Model for creating a new user

    Params
    ---------------
    user_details: dict
        The details of the user, enough to pass the AUTH SCHEMA
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
                # create user object
                user = User(**{
                    "guid": user_id,
                    "phone": user_details['username'],
                    "authentication": [user_authentication]
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
        session.remove()
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
        session.remove()
    return response

# READ


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
        session.remove()
    return response


def get_addresses(user_id):
    """
    Function to get all the addresses of the user

    Returns
    -----------
    Array of addresses, empty array if no addresses are found
    """
    response = deepcopy(NOT_FOUND)
    response['payload']['addresses'] = []
    session = SESSION()
    try:
        result, session = find_record(Address, session, {
            "user_id": user_id
        }, False)
        if result:
            response = deepcopy(RECORD_FOUND)
            response['payload']['addresses'] = [
                item.serialize for item in result]
    except Exception as exp:
        session.rollback()
        response = deepcopy(EXCEPTION_RES)
        response['payload']['description'] = repr(exp)
    session.remove()
    return response

# UPDATE


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
    response = deepcopy(NOT_FOUND)
    session = SESSION()
    try:
        user, session = find_record(User, session, {
            "guid": user_id
        })
        if user:
            for key, value in user_details.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            session.commit()
            response = deepcopy(GENERIC_SUCCESS)
    except Exception as exp:
        session.rollback()
        response = deepcopy(EXCEPTION_RES)
        response['payload']['description'] = repr(exp)
    session.remove()
    return response


# DELETE

def delete_user(user_id):
    """
    TODO
    Function to delete an user from the system

    user_id: String
        The user_id to remove from the system

    Caution: Remove dangling references as well
    """
    return


def delete_users(users):
    """
    TODO
    Function to delete a lot of users from the system

    users: list
        List of users to be deleted from the system

    Caution: Remove dangling references as well
    """
    return
