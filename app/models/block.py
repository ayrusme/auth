import uuid
from copy import deepcopy
from datetime import datetime

from database.engine import SESSION, find_record
from database.validator import BLOCK_VALIDATOR
from helpers.codes import (BAD_REQUEST, EXCEPTION_RES, GENERIC_SUCCESS,
                           NOT_FOUND, RECORD_FOUND)

from . import Apartment, Block


def add_block(user_id, block):
    """
    Model for creating a new block

    Params
    ---------------
    block: dict
    """
    response = deepcopy(BAD_REQUEST)
    # Validate the incoming details
    if BLOCK_VALIDATOR.is_valid(block):
        session = SESSION()
        try:
            # TODO don't add BLOCK if same already exists LOW_PRIORITY
            block = BLOCK_VALIDATOR.validate(
                block)
            block = Block(
                **{
                    "guid": uuid.uuid4().hex,
                    "created_by": user_id,
                    "modified_by": user_id,
                    "created_at": datetime.now(),
                    "updated_at": datetime.now(),
                }, **block)
            session.add(block)
            session.commit()
            response = deepcopy(GENERIC_SUCCESS)
            response['payload']['result'] = block.serialize
        except Exception as exp:
            session.rollback()
            response = deepcopy(EXCEPTION_RES)
            response['payload']['description'] = repr(exp)
        SESSION.remove()
    return response


def update_block():
    pass


def get_block(block_filter):
    """
    get blocks

    block_filter: dict
        Filter, duh
    """
    response = deepcopy(NOT_FOUND)
    try:
        session = SESSION()
        result, session = find_record(
            model=Block,
            session=session,
            filter_dict=block_filter,
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


def delete_block_by_id():
    pass
