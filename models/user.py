#!/usr/bin/python3
"""
defines class of user
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Definitions of User class
    Representation
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
