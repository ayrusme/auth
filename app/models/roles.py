"""
This file contains all the roles for the system
"""

# Internal Roles

VADER_ROLE_ID = "8a3aba91-c925-588b-90ec-d2cd58f73c57"
TROOPER_ROLE_ID = "5ab57aa8-3e92-53c5-ab19-8099ccd7627a"

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

# ORG Roles

CAPTAIN_ROLE_ID = "34625bdb-2ab5-4f5e-99a9-84e5d270ccb6"
ENSIGN_ROLE_ID = "e023f259-1067-4565-9a97-c08b026015dd"

CAPTAIN = {
    "guid": CAPTAIN_ROLE_ID,
    "role_name": "CAPTAIN",
    "description": "Commands the forces of the organisation"
}

ENSIGN = {
    "guid": ENSIGN_ROLE_ID,
    "role_name": "ENSIGN",
    "description": "Works under the captain"
}

# EXTERNAL Roles

REBEL_ROLE_ID = "649a4be4-673d-52be-b64a-6a7fed720bdf"

REBEL = {
    "guid": REBEL_ROLE_ID,
    "role_name": "REBEL",
    "description": "The rebel scum are at tantooine!"
}

ALL_ROLES = {
    'VADER': VADER,
    'STORM_TROOPER': STORM_TROOPER,
    'CAPTAIN': CAPTAIN,
    'ENSIGN': ENSIGN,
    'REBEL': REBEL
}
