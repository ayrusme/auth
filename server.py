"""
The file to start the server for Project Astrix
"""
from sanic import Sanic, Blueprint
from sanic.response import json

from auth.auth import auth_wrapper
from helpers import config, codes

app = Sanic(__name__)
blueprint = Blueprint(codes.ROUTE_VERSION_V1)

@blueprint.route('/ping', methods=['GET'])
async def homepage(request):
    return json({'status': 'alive'})

if __name__ == '__main__':
    app.blueprint(blueprint)
    app.run(
        host=config.SERVER_URL,
        port=config.SERVER_PORT
    )
