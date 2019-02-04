from copy import deepcopy

from flask import abort, jsonify, request
from flask.blueprints import Blueprint
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from helpers.codes import BAD_REQUEST, NOT_IMPLEMENTED, STORM_TROOPER, VADER
from models.user import register_user, get_user

USER_BLUEPRINT = Blueprint('user_routes_v1', __name__, url_prefix='/v1/')


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
        response = register_user(request.get_json(), VADER)
    return jsonify(response['payload']), response['status_code']


@USER_BLUEPRINT.route('/create-trooper', methods=['POST'])
def signup_admin():
    """
    Endpoint to allow users to signup
    """
    response = deepcopy(BAD_REQUEST)
    if hasattr(request, "json") and request.json is not None:
        response = register_user(request.get_json(), STORM_TROOPER)
    return jsonify(response['payload']), response['status_code']


# READ ENDPOINTS


@USER_BLUEPRINT.route('/user', methods=["GET"])
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


# MODIFY ENDPOINTS


@USER_BLUEPRINT.route('/modify-role', methods=['PUT'])
@jwt_required
def add_role():
    """
    Endpoint to allow users to modify roles
    """
    response = deepcopy(BAD_REQUEST)
    if hasattr(request, "json") and request.json is not None:
        response = deepcopy(BAD_REQUEST)
    return jsonify(response['payload']), response['status_code']
