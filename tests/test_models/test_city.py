#!/usr/bin/python3
"""
Unit test for Place class.
"""

import json
import unittest
from models.state import State
from models.city import City


class TestCityClass(unittest.TestCase):
    """
    test the State Class.
    """

    def test_attributes(self):
        """
        test instance attributes
        """

        state = State()
        city = City()

        self.assertEqual(state.name, "")
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_attributes_types(self):
        """
        test class attributes types.
        """

        state = State()
        city = City()

        self.assertIsInstance(state.name, str)
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)

    def test_attributes_setting(self):
        """
        Try setting instance attributes.
        """

        state = State()
        city = City()

        state.name = "Taraba Jalingo"
        city.name = "TransEkule"
        city.state_id = state.id
        self.assertEqual(state.name, "Taraba Jalingo")
        self.assertEqual(city.name, "TransEkule")
        self.assertNotEqual(state.name, State().name)
        self.assertNotEqual(city.name, City().name)
        self.assertNotEqual(city.state_id, City().state_id)
        self.assertEqual(city.state_id, state.id)

    def test_to_dict(self):
        """Test to dict"""
        city = City()

        self.assertNotIn("name", city.to_dict())
        self.assertNotIn("state_id", city.to_dict())

        city.name = "Ikate"
        city.state_id = State().id

        self.assertIn("name", city.to_dict())
        self.assertIn("state_id", city.to_dict())

    def test_save_method(self):
        """
        Test class save method
        """

        city = City()
        updated_at = city.updated_at

        self.assertEqual(city.updated_at, updated_at)
        city.save()
        self.assertNotEqual(city.updated_at, updated_at)

        with open("file.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        self.assertEqual(city.to_dict(), data["City." + city.id])
