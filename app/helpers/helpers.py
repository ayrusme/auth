"""
This file consists of the helper functions.
These functions will be reused throughout the project
"""
from datetime import datetime
from datetime import timezone


def CURRENT_TIME():
    """
    Returns the current UTC time
    """
    return datetime.utcnow
