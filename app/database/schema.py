"""
This file contains the schema for all the tables used in this project
"""

import sqlamp
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Index, Integer,
                        Sequence, String, Text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import deferred, relationship
from sqlalchemy.sql import func
from sqlalchemy_utils import EmailType, PasswordType, UUIDType

from helpers.helpers import CURRENT_TIME

Base = declarative_base(metaclass=sqlamp.DeclarativeMeta)


class User(Base):
    """
    The model to be used for the consumer

    USER MODEL
    --------------------------------------
    guid : uuid
        Unique ID assigned to the consumer (PK)
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
    last_login = Column(DateTime)
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

    @property
    def serialize(self):
        """
        Returns a JSON variant of the model
        """
        return {
            "guid": self.guid,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "addresses": [item.serialize for item in self.addresses]
        }


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


class Apartment(Base):
    """
    The model for having an apartment for the product
    """
    __tablename__ = "apartments"

    guid = Column(UUIDType(binary=False), primary_key=True)
    name = Column(String(30), nullable=False)
    address_line1 = Column(String(120), nullable=False)
    address_line2 = Column(String(120), nullable=True)
    city = Column(String(30), nullable=False)
    country = Column(String(20), nullable=False)
    pin_code = Column(Integer, nullable=False)
    created_by = Column(UUIDType(binary=False))
    modified_by = Column(UUIDType(binary=False))
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

    @property
    def serialize(self):
        """
        Returns a JSON variant of the model
        """
        return {
            "guid": self.guid,
            "name": self.name,
            "address_line1": self.address_line1,
            "address_line2": self.address_line2,
            "city": self.city,
            "country": self.country,
            "pin_code": self.pin_code
        }


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
        nullable=False
    )
    apartment_id = Column(
        UUIDType(binary=False), ForeignKey('apartments.guid'),
        nullable=False
    )
    address_line1 = Column(String(120), nullable=False)  # door number
    default = Column(Boolean, nullable=False, default=True)
    name = Column(String(30), nullable=False)
    created_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )
    updated_at = deferred(
        Column(
            DateTime, nullable=False,
            default=CURRENT_TIME(), onupdate=func.now(),
        ),
        group='defaults'
    )
