"""
The file to start the server for Project Astrix
"""
from sanic import Blueprint, Sanic
from sanic.response import json
from sanic_cors import CORS

from auth.auth import auth_wrapper
from config.config import SERVER_PORT, SERVER_URL
from controllers.authentication import auth_blueprint
from controllers.consumer import consumer_blueprint
from helpers.codes import ROUTE_VERSION_V1

# Create the server
app = Sanic(__name__)

# Register blueprints for controllers
app.register_blueprint(auth_blueprint)
app.register_blueprint(consumer_blueprint)

# Customary ping route


@app.route('/ping', methods=['GET'])
async def homepage(request):
    return json({'status': 'alive'})

# Start the server!
if __name__ == '__main__':
    app.run(
        host=SERVER_URL,
        port=SERVER_PORT
    )
