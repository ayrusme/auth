"""
The validation schema for the models
"""
from schema import And, Forbidden, Regex, Schema, Optional

USER_SCHEMA_VALIDATOR = Schema({
    Forbidden("guid"): And(str, len),
    Forbidden("created_at"): And(str, len),
    Forbidden("updated_at"): And(str, len),
    Optional("first_name"): And(str, len),
    Optional("last_name"): And(str, len),
    Optional("email"): Regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"),
    "phone": Regex(r"[6789]{1}[0-9]{9}"),
    Optional("addresses"): list,
    "authentication": object,
})

USER_UPDATE_VALIDATOR = Schema({
    Optional("guid"): And(str, len),
    Forbidden("created_at"): And(str, len),
    Forbidden("updated_at"): And(str, len),
    Optional("first_name"): And(str, len),
    Optional("last_name"): And(str, len),
    Optional("email"): Regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"),
    Forbidden("phone"): Regex(r"[6789]{1}[0-9]{9}"),
    Optional("addresses"): list,
    Optional("authentication"): object,
    Optional("role"): list
})

ADDRESS_SCHEMA_VALIDATOR = Schema({
    Forbidden("guid"): And(str, len),
    Forbidden("created_at"): And(str, len),
    Forbidden("updated_at"): And(str, len),
    "address_line1": And(str, len),
    Optional("address_line2"): And(str, len),
    "city": And(str, len),
    "country": And(str, len),
    "pin_code": int,
    "lat_long": And(str, len),
})

AUTHENTICATION_SCHEMA_VALIDATOR = Schema({
    Forbidden("guid"): And(str, len),
    Forbidden("created_at"): And(str, len),
    Forbidden("updated_at"): And(str, len),
    "username": And(str, len),
    "password": And(str, len),
})
