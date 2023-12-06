#!/usr/bin/python3
"""
Defines Place wey you wan go.
we no go carry you go where you no know
"""

from .base_model import BaseModel


class Place(BaseModel):
    """
    Defines the place User wants to go or borrow
    has attributes which will be tuned based on the Place
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    """def __init__(self):
        self.__dict__ = self.class.dict__"""
