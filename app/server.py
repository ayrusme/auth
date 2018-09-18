"""
The file to start the server for Project Astrix
"""
from sanic import Blueprint, Sanic
from sanic.response import json

# TODO Import controller blueprint
import app.controllers.consumer
from app.auth.auth import auth_wrapper
from app.config.config import SERVER_PORT, SERVER_URL
from app.controllers.authentication import auth_blueprint
from app.helpers.codes import ROUTE_VERSION_V1

# Create the server
app = Sanic(__name__)

# TODO register Blueprints


@app.route('/ping', methods=['GET'])
async def homepage(request):
    return json({'status': 'alive'})

app.blueprint(auth_blueprint)

if __name__ == '__main__':
    app.run(
        host=SERVER_URL,
        port=SERVER_PORT
    )
