#!/usr/bin/python3
"""
Defination the Review class for user and place
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines Review class
    Representation of place
    """

    place_id = ""
    user_id = ""
    text = ""
