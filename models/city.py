#!/usr/bin/python3
"""
Defines City class
"""

from .base_model import BaseModel


class City(BaseModel):
    """
    Defines city for user
    """

    state_id = ""
    name = ""
