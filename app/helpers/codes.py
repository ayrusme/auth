"""
This file contains all static references
"""

ROUTE_VERSION_V1 = "version1"
ERROR_STATUS = "error"

BAD_REQUEST = {
    "status_code": 400,
    "payload": {
        "status": ERROR_STATUS,
        "message": "Bad request",
        "description": "Required Parameters are missing"
    }
}
