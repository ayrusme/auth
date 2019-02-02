"""
All the codes used in authentication services
can be found here
"""
from datetime import timedelta

JWT_SECRET = "9A177231FFA3691F24EAFDC11B19D"
JWT_ALGORITHM = "HS256"
# Specify time in seconds
TOKEN_EXPIRY_DURATION = 3600
EXPIRY_DURATION = timedelta(seconds=TOKEN_EXPIRY_DURATION)
