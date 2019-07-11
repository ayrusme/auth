"""
This file contains all the roles for the system
"""

# Internal Roles

# super admin
VADER_ROLE_ID = "8a3aba91-c925-588b-90ec-d2cd58f73c57"

# normal admin
TROOPER_ROLE_ID = "5ab57aa8-3e92-53c5-ab19-8099ccd7627a"

# read only access
ENSIGN_ROLE_ID = "649a4be4-673d-52be-b64a-6a7fed720bdf"

# database models for the same
VADER = {
    "guid": VADER_ROLE_ID,
    "role_name": "VADER",
    "description": "If only you knew the power of the dark side!"
}

STORM_TROOPER = {
    "guid": TROOPER_ROLE_ID,
    "role_name": "STORM_TROOPER",
    "description": "These aren't the roles you're looking for!"
}

ENSIGN = {
    "guid": ENSIGN_ROLE_ID,
    "role_name": "ENSIGN",
    "description": "You're sweating, Ensign"
}


# link to engine to create during start
ALL_ROLES = {
    'VADER': VADER,
    'STORM_TROOPER': STORM_TROOPER,
    'ENSIGN': ENSIGN
}
