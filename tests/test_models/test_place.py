#!/usr/bin/python3
"""
Unit test for Place class.
"""

import unittest
import datetime
import json
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.city import City


class TestPlaceClass(unittest.TestCase):
    """
    test the Place Class.
    """

    def test_attributes(self):
        """
        test instance attributes
        """

        place = Place()

        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_attributes_types(self):
        """
        test class attributes types.
        """

        place = Place()

        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_attributes_setting(self):
        """
        Try setting instance attributes.
        """

        place = Place()
        user = User()
        city = City()

        place.user_id = user.id
        self.assertEqual(place.user_id, user.id)
        self.assertNotEqual(place.user_id, Place.user_id)

        place.name = "Basilica of Santa Maria"
        self.assertEqual(place.name, "Basilica of Santa Maria")
        self.assertNotEqual(place.name, Place.name)

        place.city_id = city.id
        self.assertEqual(place.city_id, city.id)

        place.description = "Beautiful and calm"
        self.assertNotEqual(place.description, "")

        place.number_rooms = 10
        self.assertNotEqual(place.number_rooms, 0)

        place.number_bathrooms = 4
        self.assertNotEqual(place.number_bathrooms, 0)

        place.price_by_night = 100
        self.assertNotEqual(place.price_by_night, 0)

        place.max_guest = 15
        self.assertNotEqual(place.max_guest, 0)

        place.longitude = 103
        self.assertNotEqual(place.longitude, 0.0)

        place.latitude = 45
        self.assertNotEqual(place.latitude, 0.0)

        place.amenity_ids = [Amenity().id for i in range(5)]
        self.assertNotEqual(place.amenity_ids, [])
        self.assertIsInstance(place.amenity_ids[0], str)

    def test_to_dict(self):
        """
        Test to_dict method.
        """

        place = Place()
        place1 = Place()
        attributes = [
            "user_id",
            "city_id",
            "name",
            "number_rooms",
            "number_bathrooms",
            "description",
            "longitude",
            "latitude",
            "max_guest",
            "price_by_night",
            "amenity_ids",
        ]
        self.assertNotEqual(place.id, place1.id)
        for attribute in attributes:
            self.assertNotIn(attribute, place.to_dict())
        self.assertNotIn("__class__", place.__dict__)

        place.user_id = User().id
        place.name = "Ibeju"
        place.city_id = City().id
        place.description = "Calm and nice"
        place.number_rooms = 4
        place.number_bathrooms = 2
        place.longitude = 99
        place.latitude = 80
        place.amenity_ids = [Amenity().id for x in range(4)]
        place.price_by_night = 500
        place.max_guest = 10

        # Tests attributes class attributes and super class instances
        # after instanciation
        for attribute in attributes:
            self.assertIn(attribute, place.to_dict())
        self.assertIn("__class__", place.to_dict())

        # Test checks updated_at created_at in dict rep and __dict__
        self.assertIsInstance(place1.to_dict()["updated_at"], str)
        self.assertIsInstance(place1.__dict__["updated_at"], datetime.datetime)
        self.assertIsInstance(place1.to_dict()["created_at"], str)
        self.assertIsInstance(place1.__dict__["created_at"], datetime.datetime)

    def test_save_method(self):
        """
        Test class save method
        """

        place = Place()
        updated_at = place.updated_at

        self.assertEqual(place.updated_at, updated_at)
        place.save()
        self.assertNotEqual(place.updated_at, updated_at)

        with open("file.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        self.assertEqual(place.to_dict(), data["Place." + place.id])
