"""
The file to start the server for Project Astrix
"""
from sanic import Sanic, Blueprint
from sanic.response import json

from auth.auth import auth_wrapper
from config.config import SERVER_URL, SERVER_PORT
from helpers.codes import ROUTE_VERSION_V1

app = Sanic(__name__)
blueprint = Blueprint(ROUTE_VERSION_V1)

@blueprint.route('/ping', methods=['GET'])
async def homepage(request):
    return json({'status': 'alive'})

if __name__ == '__main__':
    app.blueprint(blueprint)
    app.run(
        host=SERVER_URL,
        port=SERVER_PORT
    )
