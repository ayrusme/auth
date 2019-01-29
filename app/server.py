"""
The file to start the server for Project Astrix
"""
from flask import Flask, jsonify
from flask_cors import CORS

from config.config import SERVER_PORT, SERVER_URL
from controllers.authentication import auth_blueprint
from controllers.user import user_blueprint

# Create the server
APP = Flask(__name__)

CORS(APP)

# Register blueprints for controllers
APP.register_blueprint(user_blueprint)
APP.register_blueprint(auth_blueprint)


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
