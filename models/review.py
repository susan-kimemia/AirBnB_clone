#!/usr/bin/python3
"""
Defines the Review class for user and place
"""

from .base_model import BaseModel


class Review(BaseModel):
    """
    Defines Review for User
    """

    place_id = ""
    user_id = ""
    text = ""
