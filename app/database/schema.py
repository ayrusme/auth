"""
This file contains the schema for all the tables used in this project
"""
import uuid
from datetime import datetime

import sqlamp
from helpers.codes import MUGGLE
from helpers.codes import STORM_TROOPER
from helpers.codes import VADER
from helpers.helpers import CURRENT_TIME
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Index
from sqlalchemy import Integer
from sqlalchemy import Sequence
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref
from sqlalchemy.orm import deferred
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy_utils import EmailType
from sqlalchemy_utils import PasswordType
from sqlalchemy_utils import UUIDType

Base = declarative_base(metaclass=sqlamp.DeclarativeMeta)


class User(Base):
    """
    The model to be used for the consumer

    USER MODEL
    --------------------------------------
    guid : uuid
        Unique ID assigned to the consumer (PK)
    username : String
        The username of the consumer
    password : Hash(String)
        The password of the consumer, hashed and stored
    first_name : String
        First Name of the consumer
    last_name : String
        Last Name of the consumer
    email : String
        Email address of the consumer
    phone : Integer
        Phone number of the consumer
    last_login : Integer
        The timestamp of the last logged in time of the user
    created_at : Integer
        The timestamp of when the user data was created
    updated_at : Integer
        The timestamp of when the user data was updated
    """
    __tablename__ = "user"

    guid = Column(UUIDType(binary=False), primary_key=True)
    first_name = deferred(
        Column(String(255)),
    )
    last_name = deferred(
        Column(String(255)),
    )
    email = Column(EmailType)
    phone = Column(String(25), nullable=False)
    addresses = relationship('Address', lazy=True)
    authentication = relationship('UserAuthentication', backref='user')
    role = relationship('UserRole', backref='user')
    last_login = Column(DateTime, nullable=False, default=0)
    created_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults',
    )
    updated_at = deferred(
        Column(
            DateTime, nullable=False,
            default=CURRENT_TIME(), onupdate=func.now(),
        ),
        group='defaults',
    )


class UserAuthentication(Base):

    """
    This table contains users and their authentication credentials

    USER AUTHENTICATION MODEL
    -------------------------
    guid: String
        The unique ID assigned to the authentication record
    user_id: String
        The user ID for the record
    username: String
        The username associated with the user ID stored

    SEE ALSO
    -------------------------
    User
    """
    # Table name in the database
    __tablename__ = 'user_auth'

    # Columns
    guid = Column(UUIDType(binary=False), primary_key=True)
    user_id = Column(UUIDType(binary=False), ForeignKey('user.guid'))
    username = Column(String(255), nullable=False)
    password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt',
        ],
        deprecated=['md5_crypt'],
    ))
    created_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults',
    )
    updated_at = deferred(
        Column(
            DateTime, nullable=False,
            default=CURRENT_TIME(), onupdate=func.now(),
        ),
        group='defaults',
    )


class Address(Base):
    """
    The model for the address of a consumer

    ADDRESS MODEL
    -----------------------------------
    guid: String
        Unique ID assigned to the address (PK)
    user_id: String
        The user ID for which the address is stored (FK)
    address_line1: String
        The address of a particular user
    address_line1: String
        The address of a particular user
    city: String
        The city of the user
    country: String
        The country of the user
    pin_code: Integer
        The pin code of the user
    lat_long: String
        The geo-coorinates of the user
    """

    __tablename__ = "addresses"

    guid = Column(UUIDType(binary=False), primary_key=True)
    user_id = Column(
        UUIDType(binary=False), ForeignKey('user.guid'),
        nullable=False,
    )
    address_line1 = Column(String(120), nullable=False)
    address_line2 = Column(String(120), nullable=True)
    city = Column(String(30), nullable=False)
    country = Column(String(20), nullable=False)
    pin_code = Column(Integer, nullable=False)
    lat_long = Column(String(50), nullable=False)
    created_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults',
    )
    updated_at = deferred(
        Column(
            DateTime, nullable=False,
            default=CURRENT_TIME(), onupdate=func.now(),
        ),
        group='defaults',
    )


class Role(Base):
    """
    The model for the roles of the user

    ROLE MODEL
    ----------------------------------
    role_id: Integer
        The ID for the particular role
    role_name: String
        The name assigned to the particular role
    description: String
        The description for the particular role
    """

    __tablename__ = "roles"

    role_id = Column(UUIDType(binary=False), primary_key=True)
    role_name = Column(String(20), nullable=False)
    description = Column(String(100), nullable=False)
    created_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults',
    )
    updated_at = deferred(
        Column(
            DateTime, nullable=False,
            default=CURRENT_TIME(), onupdate=func.now(),
        ),
        group='defaults',
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# Add few roles


class UserRole(Base):
    """
    Model for all user roles

    User Role Model
    -------------------------
    guid: UUIDType
        The unique ID associated with the record
    user_id: String
        The user id associated with the role
    role_id: String
        The role id associated with the user
    """

    __tablename__ = 'user_role'

    guid = Column(UUIDType(binary=False), primary_key=True)
    user_id = Column(
        UUIDType(binary=False), ForeignKey('user.guid'),
        nullable=False,
    )
    role_id = Column(
        UUIDType(binary=False), ForeignKey('roles.role_id'),
        nullable=False,
    )
    created_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults',
    )
    updated_at = deferred(
        Column(
            DateTime, nullable=False,
            default=CURRENT_TIME(), onupdate=func.now(),
        ),
        group='defaults',
    )
