import uuid
from copy import deepcopy
from datetime import datetime

from database.engine import SESSION, find_record
from database.validator import APARTMENT_CREATE_VALIDATOR
from helpers.codes import (BAD_REQUEST, EXCEPTION_RES, GENERIC_SUCCESS)

from . import Apartment


def add_apartment(user_id, apartment):
    """
    Model for creating a new apartment

    Params
    ---------------
    apartment: dict
    """
    response = deepcopy(BAD_REQUEST)
    # Validate the incoming details
    if APARTMENT_CREATE_VALIDATOR.is_valid(apartment):
        session = SESSION()
        try:
            # TODO don't add apartment if same already exists LOW_PRIORITY
            apartment = APARTMENT_CREATE_VALIDATOR.validate(
                apartment)
            apartment = Apartment({
                **{
                    "guid": uuid.uuid4().hex,
                    "created_by": user_id,
                    "modified_by": user_id,
                    "created_at": datetime.now(),
                    "updated_at": datetime.now(),
                }, **apartment
            })
            session.add(apartment)
            session.commit()
            response = deepcopy(REGISTER_SUCCESS)
        except Exception as exp:
            session.rollback()
            response = deepcopy(EXCEPTION_RES)
            response['payload']['description'] = repr(exp)
        SESSION.remove()
    return response


def update_apartment():
    pass


def get_apartment(apartment_filter):
    """
    get apartments

    apartment_filter: dict
        Filter, duh
    """
    response = deepcopy(BAD_REQUEST)
    try:
        session = SESSION()
        result, session = find_record(Apartment, session, apartment_filter)
        if result:
            response = deepcopy(RECORD_FOUND)
            response['payload'] = result.serialize
    except Exception as exp:
        session.rollback()
        response = deepcopy(EXCEPTION_RES)
        response['payload']['description'] = repr(exp)
    SESSION.remove()
    return response


def delete_apartment_by_id():
    pass
