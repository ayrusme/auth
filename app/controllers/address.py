from copy import deepcopy

from flask import jsonify, request
from flask.blueprints import Blueprint
from flask_jwt_extended import (create_access_token, get_jwt_claims,
                                get_jwt_identity, jwt_required)

from helpers.codes import (BAD_REQUEST, EXCEPTION_RES, GENERIC_SUCCESS,
                           NOT_IMPLEMENTED)
from models.address import (add_address, get_address)

ADDRESS_BLUEPRINT = Blueprint(
    'address_routes_v1', __name__, url_prefix='/v1/address')
ADDRESS_INTERNAL = Blueprint(
    'address_internal_routes_v1', __name__, url_prefix='/v1/internal/address')
# CREATE ENDPOINTS


@ADDRESS_INTERNAL.route('/create-address', methods=['POST'])
@jwt_required
def create_address():
    """
    Endpoint to allow users to signup
    """
    response = deepcopy(BAD_REQUEST)
    user_id = get_jwt_identity()
    if user_id and hasattr(request, "json") and request.json is not None:
        response = add_address(user_id, request.json)
    return jsonify(response['payload']), response['status_code']


@ADDRESS_BLUEPRINT.route('/get-address', methods=['GET', 'POST'])
@jwt_required
def get_address_route():
    """
    Endpoint to allow users to signup
    """
    if request.method == 'GET':
        # TODO
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
        response = get_address(request.json)
    return jsonify(response['payload']), response['status_code']
