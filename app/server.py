"""
The file to start the server for Project Astrix
"""
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from auth.auth_codes import JWT_SECRET
from config.config import SERVER_PORT, SERVER_URL
from controllers.authentication import AUTH_BLUEPRINT
from controllers.user import USER_BLUEPRINT
from helpers.codes import TOKEN_ERROR

# Create the server
APP = Flask(__name__)

CORS(APP)

APP.config['JWT_SECRET_KEY'] = JWT_SECRET
JWT = JWTManager(APP)

# Register blueprints for controllers
APP.register_blueprint(USER_BLUEPRINT)
APP.register_blueprint(AUTH_BLUEPRINT)


@APP.route('/ping', methods=['GET'])
def homepage():
    """
    Customary PING route
    """
    return jsonify({'status': 'alive'})


@JWT.unauthorized_loader
def unauthorized(token):
    return jsonify(TOKEN_ERROR['payload']), TOKEN_ERROR['status_code']


@JWT.expired_token_loader
def unauthorized(token):
    return jsonify(TOKEN_ERROR['payload']), TOKEN_ERROR['status_code']


# Start the server!
if __name__ == '__main__':
    APP.run(
        host=SERVER_URL,
        port=SERVER_PORT,
        debug=True,
    )
