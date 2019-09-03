from copy import deepcopy

from flask import jsonify, request
from flask.blueprints import Blueprint
from flask_jwt_extended import (create_access_token, get_jwt_claims,
                                get_jwt_identity, jwt_required)

from helpers.codes import (BAD_REQUEST, EXCEPTION_RES, GENERIC_SUCCESS,
                           NOT_IMPLEMENTED)
from models.apartment import (add_apartment, get_apartment)

APARTMENT_BLUEPRINT = Blueprint(
    'user_routes_v1', __name__, url_prefix='/v1/apartment')
APARTMENT_INTERNAL = Blueprint(
    'user_routes_v1', __name__, url_prefix='/v1/internal/apartment')
# CREATE ENDPOINTS


@APARTMENT_INTERNAL.route('/create-apartment', methods=['POST'])
@jwt_required
def create_apartment():
    """
    Endpoint to allow users to signup
    """
    response = deepcopy(BAD_REQUEST)
    user_id = get_jwt_identity()
    if user_id and hasattr(request, "json") and request.json is not None:
        response = add_apartment(user_id, request.json)
    return jsonify(response['payload']), response['status_code']


@APARTMENT_BLUEPRINT.route('/get-apartment', methods=['GET', 'POST'])
@jwt_required
def get_apartment():
    """
    Endpoint to allow users to signup
    """
    if request.method == 'GET':
        return jsonify(
            {
                "message": "You can pass the following items in any combination. Anything other than these \
                    would yield results, but won't be of any use",
                "payload": {
                    "guid": {
                        "mandatory": False,
                        "type": "string"
                    },
                    "city": {
                        "mandatory": False,
                        "type": "string"
                    },
                    "country": {
                        "mandatory": False,
                        "type": "string"
                    },
                    "pin_code": {
                        "mandatory": False,
                        "type": "string"
                    },
                    "created_by": {
                        "mandatory": False,
                        "type": "string"
                    },
                    "modified_by": {
                        "mandatory": False,
                        "type": "string"
                    }
                }
            }), 200
    response = deepcopy(BAD_REQUEST)
    user_id = get_jwt_identity()
    if user_id and hasattr(request, "json") and request.json is not None:
        response = get_apartment(request.json)
    return jsonify(response['payload']), response['status_code']
