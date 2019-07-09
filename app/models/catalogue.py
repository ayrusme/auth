"""
All catalogue and item models are available here
"""

import uuid
from copy import deepcopy
from datetime import datetime

from database.engine import SESSION, find_record
from helpers.codes import (BAD_REQUEST, ENTITY_EXISTS, EXCEPTION_RES,
                           GENERIC_SUCCESS, NOT_FOUND, REBEL, RECORD_FOUND)

from . import Catalogue, CatalogueRole, Item, SystemRole


def create_catalogue(catalogue_details):
    """
    Model for creating a new catalogue

    Params
    ---------------
    catalogue_details: dict
        The details of the user, enough to pass the AUTH SCHEMA
    role: dict
        An optional parameter defining the role of the user
    """
    response = deepcopy(BAD_REQUEST)
    return response


def update_catalogue():
    return


def get_catalogue():
    return


def delete_catalogue():
    return
