"""
All catalogue and item models are available here
"""

import uuid
from copy import deepcopy
from datetime import datetime

from database.engine import SESSION, find_record
from helpers.codes import (BAD_REQUEST, ENTITY_EXISTS, EXCEPTION_RES,
                           GENERIC_SUCCESS, NOT_FOUND, REBEL, RECORD_FOUND,
                           REGISTER_SUCCESS)

from . import Catalogue, CatalogueRole, Item, SystemRole


def create_catalogue():
    return


def update_catalogue():
    return


def get_catalogue():
    return


def delete_catalogue():
    return
