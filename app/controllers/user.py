from copy import deepcopy

from flask import abort, jsonify, request
from flask.blueprints import Blueprint
from flask_jwt_extended import (create_access_token, get_jwt_claims,
                                get_jwt_identity, jwt_required)

from auth.auth import vader_wrapper
from helpers.codes import (BAD_REQUEST, EXCEPTION_RES, GENERIC_SUCCESS,
                           NOT_IMPLEMENTED)
from models.roles import ALL_ROLES
from models.user import (add_address, add_role, get_addresses, get_full_roles,
                         get_user, modify_user, register_user)

USER_BLUEPRINT = Blueprint('user_routes_v1', __name__, url_prefix='/v1/user')


# CREATE ENDPOINTS


@USER_BLUEPRINT.route('/create-rebel', methods=['POST'])
def signup():
    """
    Endpoint to allow users to signup
    """
    response = deepcopy(BAD_REQUEST)
    if hasattr(request, "json") and request.json is not None:
        response = register_user(request.get_json())
    return jsonify(response['payload']), response['status_code']


@USER_BLUEPRINT.route('/create-vader', methods=['POST'])
def signup_super_admin():
    """
    Endpoint to allow users to signup
    """
    response = deepcopy(BAD_REQUEST)
    if hasattr(request, "json") and request.json is not None:
        response = register_user(request.get_json(), ALL_ROLES['VADER'])
    return jsonify(response['payload']), response['status_code']


@USER_BLUEPRINT.route('/create-trooper', methods=['POST'])
@vader_wrapper
def signup_admin():
    """
    Endpoint to allow users to signup
    """
    response = deepcopy(BAD_REQUEST)
    if hasattr(request, "json") and request.json is not None:
        response = register_user(request.get_json(), ALL_ROLES['TROOPER'])
    return jsonify(response['payload']), response['status_code']


@USER_BLUEPRINT.route('/add-address', methods=['POST'])
@jwt_required
def create_address():
    """
    Endpoint to add address to the current user
    """
    response = deepcopy(BAD_REQUEST)
    if hasattr(request, "json") and request.json is not None:
        user_id = get_jwt_identity()
        if user_id:
            response = add_address(user_id, request.json)
    return jsonify(response['payload']), response['status_code']

# READ ENDPOINTS


@USER_BLUEPRINT.route('/', methods=["GET"])
@jwt_required
def get_self():
    """
    Endpoint to get the current user information
    """
    user_id = get_jwt_identity()
    response = get_user({
        "guid": user_id
    })
    return jsonify(response['payload']), response['status_code']


@USER_BLUEPRINT.route('/addresses', methods=["GET"])
@jwt_required
def get_address():
    """
    Endpoint to get the current user information
    """
    user_id = get_jwt_identity()
    response = get_addresses(user_id)
    return jsonify(response['payload']), response['status_code']


@USER_BLUEPRINT.route('/all-roles', methods=["GET"])
@jwt_required
@vader_wrapper
def get_all_roles():
    """
    Endpoint which will return all the roles
    """
    response = deepcopy(GENERIC_SUCCESS)
    response['payload']['roles'] = ALL_ROLES
    return jsonify(response['payload']), response['status_code']


@USER_BLUEPRINT.route('/roles', methods=["GET"])
@jwt_required
def get_user_roles():
    """
    Endpoint which will return all the roles for the given user
    """
    response = deepcopy(GENERIC_SUCCESS)
    user_id = get_jwt_identity()
    response['payload']['roles'] = get_full_roles(user_id)
    return jsonify(response['payload']), response['status_code']

# MODIFY ENDPOINTS


@USER_BLUEPRINT.route('/update-role', methods=['POST'])
@jwt_required
@vader_wrapper
def add_role():
    """
    Endpoint to allow users to modify roles
    """
    response = deepcopy(BAD_REQUEST)
    if hasattr(request, "json") and request.json is not None:
        response = add_role(request.json)
    return jsonify(response['payload']), response['status_code']


@USER_BLUEPRINT.route('/update-address', methods=['POST'])
@jwt_required
def update_address():
    """
    Endpoint to update address to the current user
    """
    response = deepcopy(NOT_IMPLEMENTED)
    if hasattr(request, "json") and request.json is not None:
        response = deepcopy(NOT_IMPLEMENTED)
    return jsonify(response['payload']), response['status_code']


@USER_BLUEPRINT.route('/update-user', methods=['POST'])
@jwt_required
def update_user():
    """
    Endpoint to update the details of the current user
    """
    response = deepcopy(NOT_IMPLEMENTED)
    if hasattr(request, "json") and request.json is not None:
        user_id = get_jwt_identity()
        response = modify_user(user_id, request.json)
    return jsonify(response['payload']), response['status_code']
