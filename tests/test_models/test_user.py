#!/bin/python3
"""
Contains Unit test for User Class.
"""

import unittest
import json
import datetime
from models.user import User


class TestUserClass(unittest.TestCase):
    """
    Test User Class attributes and methods.
    """

    def test_attributes(self):
        """
        Tests class attributes and also assigning values to em
        """

        user = User()
        user1 = User()

        # test value types
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        self.assertIsInstance(user.password, str)

        # Tests Values before assignment
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

        # Tests Values after assignment
        user.first_name = "John"
        user.last_name = "Doe"
        user.password = "Kilode gan"
        user.email = "emilokan@gmail.com"
        self.assertNotEqual(user.email, "")
        self.assertNotEqual(user.password, "")
        self.assertNotEqual(user.first_name, "")
        self.assertNotEqual(user.last_name, "")
        user.id = "1223-3678-5thg-dkif"
        self.assertNotEqual(user.id, "")

        user1.first_name = "Zach"
        user1.password = "After Money na Money"
        self.assertEqual(user1.email, "")
        self.assertNotEqual(user1.password, "")
        self.assertNotEqual(user1.first_name, "")
        self.assertEqual(user1.last_name, "")

    def test_to_dict(self):
        """
        Test to_dict method.
        """

        user = User()
        user1 = User()

        self.assertNotIn("password", user.to_dict())
        self.assertNotIn("first_name", user.to_dict())
        self.assertNotIn("last_name", user.to_dict())
        self.assertNotIn("email", user.to_dict())
        self.assertNotIn("__class__", user.__dict__)

        user.first_name = "John"
        user.last_name = "Doe"
        user.password = "Kilode gan"
        user.email = "emilokan@gmail.com"

        # Tests attributes class attributes and super class instances
        # after instanciation
        self.assertIn("password", user.to_dict())
        self.assertIn("first_name", user.to_dict())
        self.assertIn("last_name", user.to_dict())
        self.assertIn("email", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

        # Test checks updated_at created_at in dict rep and __dict__
        self.assertIsInstance(user1.to_dict()["updated_at"], str)
        self.assertIsInstance(user1.__dict__["updated_at"], datetime.datetime)
        self.assertIsInstance(user1.to_dict()["created_at"], str)
        self.assertIsInstance(user1.__dict__["created_at"], datetime.datetime)

    def test_save_method(self):
        """
        Test class save method
        """

        user = User()
        updated_at = user.updated_at

        self.assertEqual(user.updated_at, updated_at)
        user.save()
        self.assertNotEqual(user.updated_at, updated_at)

        with open("file.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        self.assertIn(user.to_dict(), data.values())
        self.assertEqual(user.to_dict(), data["User." + user.id])
