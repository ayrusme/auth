"""
This file contains the schema for all the tables used in this project
"""

import uuid
from datetime import datetime, timezone

import sqlamp
from sqlalchemy import (Column, ForeignKey, Index, Integer, Sequence, String,
                        Text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import deferred, relationship

from sqlalchemy_utils import UUIDType, EmailType
from app.helpers.helpers import CURRENT_TIME
Base = declarative_base(metaclass=sqlamp.DeclarativeMeta)


"""
The model to be used for the consumer

CONSUMER MODEL
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

# TODO Hash Password and Store


class Consumer(Base):
    __tablename__ = "consumer"

    guid = Column(UUIDType(binary=False), primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    first_name = deferred(
        Column(String(255), nullable=False)
    )
    last_name = deferred(
        Column(String(255), nullable=False)
    )
    email = Column(EmailType)
    phone = Column(Integer, nullable=False)
    addresses = relationship('addresses', backref='consumer', lazy=True)
    last_login = Column(Integer, nullable=False, default=0)
    created_at = deferred(
        Column(Integer, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )
    updated_at = deferred(
        Column(Integer, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )

    def __init__(self, username, password, first_name,
                 last_name, email, phone, addresses,
                 last_login, created_at, updated_at):
        self.username = username
        self.password = password
        self.addresses = addresses
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.last_login = last_login
        self.created_at = created_at
        self.updated_at = updated_at


"""
The model for the address of a consumer

ADDRESS MODEL
-----------------------------------
guid - Unique ID assigned to the address (PK)
address - The address of a particular user
user_id - The user ID for which the address is stored (FK)
"""


class Address(Base):
    __tablename__ = "addresses"

    guid = Column(UUIDType(binary=False), primary_key=True)
    address = Column(String(120), nullable=False)
    person_id = Column(Integer, ForeignKey('consumer.guid'),
                       nullable=False)
    created_at = deferred(
        Column(Integer, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )
    updated_at = deferred(
        Column(Integer, nullable=False, default=CURRENT_TIME()),
        group='defaults'
    )

    def __init__(self, address, person_id, created_at, updated_at):
        self.address = address
        self.person_id = person_id
        self.created_at = created_at
        self.updated_at = updated_at
