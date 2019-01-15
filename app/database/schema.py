"""
This file contains the schema for all the tables used in this project
"""

import uuid
from datetime import datetime, timezone

import sqlamp
from sqlalchemy import (Column, DateTime, ForeignKey, Index, Integer, Sequence,
                        String, Text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, deferred, relationship
from sqlalchemy_utils import EmailType, PasswordType, UUIDType

from app.helpers.helpers import CURRENT_TIME

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
        Column(String(255), nullable=False)
    )
    last_name = deferred(
        Column(String(255), nullable=False)
    )
    email = Column(EmailType)
    phone = Column(String(25), nullable=False)
    addresses = relationship('Address', backref='user', lazy=True)
    authentication = relationship('UserAuthentication', backref='user')
    role = relationship('UserRole', backref='user')
    last_login = Column(DateTime, nullable=False, default=0)
    created_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )
    updated_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )

    def __init__(self, guid, first_name, last_name, email,
                 phone, addresses, authentication, role, last_login, 
                 created_at, updated_at):
        self.guid = guid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.last_login = last_login
        self.addresses = addresses
        self.authentication = authentication
        self.role = role
        self.created_at = created_at
        self.updated_at = updated_at


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
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ))
    created_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )
    updated_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )

    def __init__(self, guid, user_id, username,
                 password, created_at, updated_at):
        self.guid = guid
        self.user_id = user_id
        self.username = username
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at


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
    user_id = Column(UUIDType(binary=False), ForeignKey('user.guid'),
                     nullable=False)
    address_line1 = Column(String(120), nullable=False)
    address_line2 = Column(String(120), nullable=True)
    city = Column(String(30), nullable=False)
    country = Column(String(20), nullable=False)
    pin_code = Column(Integer, nullable=False)
    lat_long = Column(String(50), nullable=False)
    created_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )
    updated_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )

    def __init__(self, guid, user_id, address_line1,
                 address_line2, city, country, pin_code,
                 lat_long, created_at, updated_at):
        self.guid = guid
        self.user_id = user_id
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.city = city
        self.country = country
        self.pin_code = pin_code
        self.lat_long = lat_long
        self.created_at = created_at
        self.updated_at = updated_at


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
    description = Column(String(20), nullable=False)
    created_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )
    updated_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )

    def __init__(self, role_id, role_name,
                 description, created_at, updated_at):
        self.role_id = role_id
        self.role_name = role_name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at


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
    user_id = Column(UUIDType(binary=False), ForeignKey('user.guid'),
                     nullable=False)
    role_id = Column(UUIDType(binary=False), ForeignKey('roles.role_id'),
                     nullable=False)
    created_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )
    updated_at = deferred(
        Column(DateTime, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )

    def __init__(self, guid, user_id,
                 role_id, created_at, updated_at):
        self.guid = guid
        self.user_id = user_id
        self.role_id = role_id
        self.created_at = created_at
        self.updated_at = updated_at
