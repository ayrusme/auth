"""
The file to hold the configuration for the project
"""
import json
import os

with open('config.json') as file:
    DATA = json.load(file)

    if "SETUP" in os.environ:
        try:
            DATA = DATA.get(os.environ["SETUP"])
        except Exception:
            DATA = DATA.get("LOCAL")

    # read server configuration
    SERVER_URL = DATA['SERVER']['URL'] if DATA['SERVER']['URL'] else "127.0.0.1"
    SERVER_PORT = DATA['SERVER']['PORT'] if DATA['SERVER']['PORT'] else 8001

    # read database configuration
    DATABASE_TYPE = DATA['DATABASE']['TYPE'].lower(
    ) if DATA['DATABASE']['TYPE'] else "mysql"
    DATABASE_NAME = DATA['DATABASE']['NAME'].lower(
    ) if DATA['DATABASE']['NAME'] else "astrix"
    DATABASE_DRIVER = DATA['DATABASE']['DRIVER'].lower(
    ) if DATA['DATABASE']['DRIVER'] else "pymysql"
    HOST = DATA['DATABASE']['HOST'].lower(
    ) if DATA['DATABASE']['HOST'] else "localhost"
    PORT = DATA['DATABASE']['PORT'] if DATA['DATABASE']['PORT'] else "3306"
    USERNAME = DATA['DATABASE']['USERNAME'] if DATA['DATABASE']['USERNAME'] else "root"
    PASSWORD = DATA['DATABASE']['PASSWORD'] if DATA['DATABASE']['PASSWORD'] else "root"

    # TODO If password exists, add password to URI
    # construct the URI
    DB_URI = "{TYPE}+{DRIVER}://{USERNAME}@{HOST}:{PORT}/{NAME}".format(
        TYPE=DATABASE_TYPE,
        DRIVER=DATABASE_DRIVER,
        USERNAME=USERNAME,
        HOST=HOST,
        PORT=PORT,
        NAME=DATABASE_NAME,
    )

    LOG_LEVEL = DATA['LOG']['LEVEL'] if DATA['LOG']['LEVEL'] else "INFO"
    LOG_FILE = DATA['LOG']['FILE'] if DATA['LOG']['FILE'] else "logs.log"
