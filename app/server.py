"""
The file to start the server for Project Astrix
"""
from flask import Blueprint, Flask, jsonify, request
from flask_cors import CORS

from auth.auth import auth_wrapper
from config.config import SERVER_PORT, SERVER_URL
from controllers.authentication import auth_blueprint
from controllers.user import user_blueprint
from helpers.codes import ROUTE_VERSION_V1

# Create the server
app = Flask(__name__)

# Register blueprints for controllers
app.register_blueprint(user_blueprint)
app.register_blueprint(auth_blueprint)

@app.route('/ping', methods=['GET'])
def homepage():
    """
    Customary PING route
    """
    return jsonify({'status': 'alive'})

# Start the server!
if __name__ == '__main__':
    app.run(
        host=SERVER_URL,
        port=SERVER_PORT,
        debug=True
    )
