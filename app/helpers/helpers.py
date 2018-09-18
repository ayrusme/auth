"""
This file consists of the helper functions.
These functions will be reused throughout the project
"""
from datetime import datetime, timezone

def CURRENT_TIME():
    return int(datetime.now(tz=timezone.utc).timestamp())
