"""
This file contains all static references
"""
# Roles
VADER = {
    "role_id": "8a3aba91c925588b90ecd2cd58f73c57",
    "role_name": "VADER",
    "description": "If only you knew the power of the dark side!",
}

STORM_TROOPER = {
    "role_id": "5ab57aa83e9253c5ab198099ccd7627a",
    "role_name": "STORM_TROOPER",
    "description": "These aren't the roles you're looking for!",
}

MUGGLE = {
    "role_id": "649a4be4673d52beb64a6a7fed720bdf",
    "role_name": "MUGGLE",
    "description": "Life's a struggle when you're a muggle",
}


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
        "description": "Bad username or password"
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
