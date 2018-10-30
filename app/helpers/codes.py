"""
This file contains all static references
"""

ROUTE_VERSION_V1 = "version1"

# Status Messages
ERROR_STATUS = "error"
SUCCESS_STATUS = "success"

# Status Codes
SUCCESS_STATUS_CODE = 200
BAD_REQUEST = 400
NOT_AUTHENTICATED = 401
NOT_AUTHORIZED = 403

# Response packets
BAD_REQUEST = {
    "status_code": BAD_REQUEST,
    "payload": {
        "status": ERROR_STATUS,
        "message": "Bad request",
        "description": "Required Parameters are missing"
    }
}

NOT_AUTHENTICATED = {
    "status_code": NOT_AUTHENTICATED,
    "status": ERROR_STATUS,
    "message": "Not Authenticated",
    "description": "Bad username or password"
}

NOT_AUTHORIZED = {
    "status_code": NOT_AUTHORIZED,
    "status": ERROR_STATUS,
    "message": "Unauthorized",
    "description": "You do not have access for this particular resource"
}

AUTH_OKAY = {
    "status_code": SUCCESS_STATUS_CODE,
    "status": SUCCESS_STATUS,
    "message": "Auth success",
    "description": "Move along!"
}
