"""
The file to start the server for Project Astrix
"""
from flask import Flask, jsonify
from flask_cors import CORS

from auth.auth_codes import JWT_SECRET
from config.config import SERVER_PORT, SERVER_URL
from controllers.authentication import AUTH_BLUEPRINT
from controllers.user import USER_BLUEPRINT
from flask_jwt_extended import JWTManager

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


# Start the server!
if __name__ == '__main__':
    APP.run(
        host=SERVER_URL,
        port=SERVER_PORT,
        debug=True,
    )
