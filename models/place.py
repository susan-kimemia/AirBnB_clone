#!/usr/bin/python3
"""
Defines a destination with careful consideration
We ensure not to take you where you're unfamiliar.
"""

from .base_model import BaseModel


class Place(BaseModel):
    """
    Defines the desired location a user wants to explore or reside.
    It has attributes that can be customized based on the specific place.
    """

    city_id = ""    # Identifier for the city
    user_id = ""    # Identifier for the user
    name = ""   # Name of the place
    description = ""    # Description of the place
    number_rooms = 0    # Number of rooms available
    number_bathrooms = 0    # Number of bathrooms available
    max_guest = 0   # Maximum number of guests allowed
    price_by_night = 0  # Price per night for the place
    latitude = 0.0  # Latitude coordinate of the place
    longitude = 0.0  # Longitude coordinate of the place
    amenity_ids = []    # List of amenity identifiers for the place

    """
    Initializes an instance of Place.
    The attribute dictionary is set based on
    the class's dictionary
    """
