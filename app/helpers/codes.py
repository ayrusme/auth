"""
This file contains all static references
"""
# Roles
VADER_ROLE_ID = "8a3aba91-c925-588b-90ec-d2cd58f73c57"
TROOPER_ROLE_ID = "5ab57aa8-3e92-53c5-ab19-8099ccd7627a"
REBEL_ROLE_ID = "649a4be4-673d-52be-b64a-6a7fed720bdf"

VADER = {
    "role_id": VADER_ROLE_ID,
    "role_name": "VADER",
    "description": "If only you knew the power of the dark side!"
}

STORM_TROOPER = {
    "role_id": TROOPER_ROLE_ID,
    "role_name": "STORM_TROOPER",
    "description": "These aren't the roles you're looking for!"
}

REBEL = {
    "role_id": REBEL_ROLE_ID,
    "role_name": "REBEL",
    "description": "The rebel scum are at tantooine!"
}

ALL_ROLES = [VADER, STORM_TROOPER, REBEL]

# Status Messages
ERROR_STATUS = "error"
SUCCESS_STATUS = "success"

# Status Codes
SUCCESS_STATUS_CODE = 200
BAD_REQUEST_STATUS_CODE = 400
NOT_AUTHENTICATED_STATUS_CODE = 401
NOT_AUTHORIZED_STATUS_CODE = 403
NOT_FOUND_STATUS_CODE = 404
CONFLICT_STATUS_CODE = 409
SERVER_FAILURE_STATUS_CODE = 500

# Response packets
NOT_IMPLEMENTED = {
    "status_code": BAD_REQUEST_STATUS_CODE,
    "payload": {
        "status": ERROR_STATUS,
        "message": "This method has not been implemented yet!",
        "description": "Please let me know if it is needed"
    }
}

NOT_FOUND = {
    "status_code": NOT_FOUND_STATUS_CODE,
    "payload": {
        "status": ERROR_STATUS,
        "message": "I am not able to find this",
        "description": "Check the request and try again!"
    }
}

RECORD_FOUND = {
    "status_code": SUCCESS_STATUS_CODE,
    "payload": {
    }
}

BAD_REQUEST = {
    "status_code": BAD_REQUEST_STATUS_CODE,
    "payload": {
        "status": ERROR_STATUS,
        "message": "Bad request",
        "description": "Required Parameters are missing",
    },
}

NOT_AUTHENTICATED = {
    "status_code": NOT_AUTHENTICATED_STATUS_CODE,
    "payload": {
        "status": ERROR_STATUS,
        "message": "Not Authenticated",
        "description": "You provided a bad username or password"
    }
}

TOKEN_ERROR = {
    "status_code": NOT_AUTHENTICATED_STATUS_CODE,
    "payload": {
        "status": ERROR_STATUS,
        "message": "Token Trouble",
        "description": "The token is bad, boy!"
    }
}

NOT_AUTHORIZED = {
    "status_code": NOT_AUTHORIZED_STATUS_CODE,
    "payload": {
        "status": ERROR_STATUS,
        "message": "Unauthorized",
        "description": "These are not the droids you're looking for"
    }
}

AUTH_OKAY = {
    "status_code": SUCCESS_STATUS_CODE,
    "payload": {
        "status": SUCCESS_STATUS,
        "message": "Auth success",
        "description": "Move along!"
    }
}

REGISTER_SUCCESS = {
    "status_code": SUCCESS_STATUS_CODE,
    "payload": {
        "status": SUCCESS_STATUS,
        "message": "User Successfully Registered",
        "description": "You called the register endpoint. The user was registered."
    }
}

ENTITY_EXISTS = {
    "status_code": CONFLICT_STATUS_CODE,
    "payload": {
        "status": ERROR_STATUS,
        "message": "The entity already exists!",
        "description": "The entity exists! We cannot create an entity that already exists!"
    }
}

GENERIC_SUCCESS = {
    "status_code": SUCCESS_STATUS_CODE,
    "payload": {
        "status": SUCCESS_STATUS,
        "message": "Good to go, champ!",
        "description": "The operation you called for was a huge success! Have a beer on me."
    }
}

EXCEPTION_RES = {
    "status_code": SERVER_FAILURE_STATUS_CODE,
    "payload": {
        "status": ERROR_STATUS,
        "message": "Something really bad happened!",
        "description": ""
    }
}
