#!/usr/bin/python3
"""
Unit test for Place class.
"""

import json
import unittest
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """
    test the State Class.
    """

    def test_attributes(self):
        """
        test instance attributes
        """

        amenity = Amenity()

        self.assertEqual(amenity.name, "")

    def test_attributes_types(self):
        """
        test class attributes types.
        """

        amenity = Amenity()

        self.assertIsInstance(amenity.name, str)

    def test_attributes_setting(self):
        """
        Try setting instance attributes.
        """

        amenity = Amenity()
        amenity1 = Amenity()

        amenity.name = "Wifi"
        amenity1.name = "Play station"
        self.assertEqual(amenity.name, "Wifi")
        self.assertEqual(amenity1.name, "Play station")
        self.assertNotEqual(amenity.name, Amenity().name)
        self.assertNotEqual(amenity1.name, Amenity().name)

    def test_to_dict(self):
        """Test to dict"""
        amenity = Amenity()

        self.assertNotIn("name", amenity.to_dict())

        amenity.name = "Fire detector"

        self.assertIn("name", amenity.to_dict())

    def test_save_method(self):
        """
        Test class save method
        """

        amenity = Amenity()
        updated_at = amenity.updated_at

        self.assertEqual(amenity.updated_at, updated_at)
        amenity.save()
        self.assertNotEqual(amenity.updated_at, updated_at)

        with open("file.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        self.assertEqual(amenity.to_dict(), data["Amenity." + amenity.id])
