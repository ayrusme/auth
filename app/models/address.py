import uuid
from copy import deepcopy
from datetime import datetime

from database.engine import SESSION, find_record
from database.validator import ADDRESS_VALIDATOR
from helpers.codes import (BAD_REQUEST, EXCEPTION_RES, GENERIC_SUCCESS,
                           NOT_FOUND, RECORD_FOUND)

from . import Address, Apartment, Block


def add_address(user_id, address):
    """
    Model for creating a new address

    Params
    ---------------
    address: dict
    """
    response = deepcopy(BAD_REQUEST)
    # Validate the incoming details
    address['user_id'] = user_id
    if ADDRESS_VALIDATOR.is_valid(address):
        session = SESSION()
        try:
            # TODO don't add BLOCK if same already exists LOW_PRIORITY
            address = ADDRESS_VALIDATOR.validate(
                address)
            address["guid"] = uuid.uuid4().hex
            address["created_at"] = datetime.now()
            address["updated_at"] = datetime.now()
            address = Address(**address)
            session.add(address)
            session.commit()
            response = deepcopy(GENERIC_SUCCESS)
            # response['payload']['result'] = address.serialize TODO
        except Exception as exp:
            session.rollback()
            response = deepcopy(EXCEPTION_RES)
            response['payload']['description'] = repr(exp)
        SESSION.remove()
    return response


def update_address():
    pass


def get_address(address_filter):
    """
    get addresss

    address_filter: dict
        Filter, duh
    """
    response = deepcopy(NOT_FOUND)
    try:
        session = SESSION()
        result, session = find_record(
            model=Address,
            session=session,
            filter_dict=address_filter,
            first_only=False
        )
        if result:
            response = deepcopy(RECORD_FOUND)
            response['payload'] = [item.serialize for item in result]
    except Exception as exp:
        session.rollback()
        response = deepcopy(EXCEPTION_RES)
        response['payload']['description'] = repr(exp)
    SESSION.remove()
    return response


def delete_address_by_id():
    pass
