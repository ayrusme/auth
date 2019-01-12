"""
The validation schema for the models 
"""
from schema import And, Forbidden, Optional, Regex, Schema

USER_SCHEMA = Schema({
    Forbidden("guid"): And(str, len),
    Forbidden("created_at"): And(str, len),
    Forbidden("updated_at"): And(str, len),
    "first_name": And(str, len),
    "last_name": And(str, len),
    "email": Regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"),
    "phone": Regex(r"[6789]{1}[0-9]{9}"),
    "addresses": list,
    "authentication": object
})

ADDRESS_SCHEMA = {
    Forbidden("guid"): And(str, len),
    Forbidden("created_at"): And(str, len),
    Forbidden("updated_at"): And(str, len),
    "address_line1": And(str, len),
    "address_line2": And(str, len),
    "city": And(str, len),
    "country": And(str, len),
    "pin_code": int,
    "lat_long": And(str, len)
}

AUTHENTICATION_SCHEMA = {
    Forbidden("guid"): And(str, len),
    Forbidden("created_at"): And(str, len),
    Forbidden("updated_at"): And(str, len),
    "username": And(str, len),
    "password": And(str, len)
}