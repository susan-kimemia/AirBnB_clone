#!/usr/bin/python3
"""
Unit test for Place class.
"""

import json
import unittest
from models.place import Place
from models.user import User
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """
    test the Review Class.
    """

    def test_attributes(self):
        """
        test instance attributes
        """

        review = Review()

        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attributes_types(self):
        """
        test class attributes types.
        """

        review = Review()

        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_attributes_setting(self):
        """
        Try setting instance attributes.
        """

        review = Review()
        user = User()
        place = Place()

        review.place_id = place.id
        review.user_id = user.id
        review.text = "Satisfied"
        self.assertEqual(review.place_id, place.id)
        self.assertEqual(review.user_id, user.id)
        self.assertEqual(review.text, "Satisfied")
        self.assertNotEqual(review.place_id, Place().id)
        self.assertNotEqual(review.user_id, User().id)
        self.assertNotEqual(review.text, Review().id)

    def test_to_dict(self):
        """Test to dict"""
        review = Review()

        self.assertNotIn("place_id", review.to_dict())
        self.assertNotIn("user_id", review.to_dict())
        self.assertNotIn("text", review.to_dict())

        review.place_id = "e343-43e3-456t-hy54"
        review.user_id = "dr34-h567-t534-7y64"
        review.text = "Will book again"

        self.assertIn("place_id", review.to_dict())
        self.assertIn("user_id", review.to_dict())
        self.assertIn("text", review.to_dict())

    def test_save_method(self):
        """
        Test class save method
        """

        review = Review()
        updated_at = review.updated_at

        self.assertEqual(review.updated_at, updated_at)
        review.save()
        self.assertNotEqual(review.updated_at, updated_at)

        with open("file.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        self.assertEqual(review.to_dict(), data["Review." + review.id])
