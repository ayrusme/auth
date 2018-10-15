"""
The file to hold the configuration for the project
"""
import json

with open ('config.json') as file:
    data = json.load(file)
    
    # read server configuration
    SERVER_URL = data['SERVER']['URL'] if data['SERVER']['URL'] else "127.0.0.1"
    SERVER_PORT =  data['SERVER']['PORT'] if data['SERVER']['PORT'] else 8001

    # read database configuration
    DATABASE_TYPE = data['DATABASE']['TYPE'].lower() if data['DATABASE']['TYPE'] else "mysql"
    DATABASE_NAME = data['DATABASE']['NAME'].lower() if data['DATABASE']['NAME'] else "astrix"
    DATABASE_DRIVER = data['DATABASE']['DRIVER'].lower() if data['DATABASE']['DRIVER'] else "pymysql"
    HOST = data['DATABASE']['HOST'].lower() if data['DATABASE']['HOST'] else "localhost"
    PORT = data['DATABASE']['PORT'] if data['DATABASE']['PORT'] else "3306"
    USERNAME = data['DATABASE']['USERNAME'] if data['DATABASE']['USERNAME'] else "root"
    PASSWORD = data['DATABASE']['PASSWORD'] if data['DATABASE']['PASSWORD'] else "root"

    # construct the URI
    DB_URI = "{TYPE}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{NAME}".format(
        TYPE=DATABASE_TYPE,
        DRIVER=DATABASE_DRIVER,
        USERNAME=USERNAME,
        PASSWORD=PASSWORD,
        HOST=HOST,
        PORT=PORT,
        NAME=DATABASE_NAME
    )

    LOG_LEVEL = data['LOG']['LEVEL'] if data['LOG']['LEVEL'] else "INFO"
    LOG_FILE = data['LOG']['FILE'] if data['LOG']['FILE'] else "logs.log"
