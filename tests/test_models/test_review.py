#! /usr/bin/python3

import unittest
import os

from models import storage
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """
    Unit test class for Review
    """

    def setUp(self):
        """
        Creates a temporary test file and saves it.
        """
        # Create a temporary test file
        with open("test_file.json", "w") as f:
            pass

        # Save the file
        storage.save()
    
    def tearDown(self):
        """
        Removes the temporary test file if it exists.
        """
        try:
            # Try removing the test file
            os.remove("test_file.json")
        except FileNotFoundError:
            # Ignore if the file doesn't exist
            pass
    
    def test_review_attributes(self):
        """
        Tests the default values of Review attributes.
        """
        # Create a new Review instance
        review = Review()

        # Assert that place_id, user_id, and text are empty strings
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
    
    def test_review_inherits_from_basemodel(self):
        """
        Tests that Review inherits from BaseModel.
        """
        # Create a new Review instance
        review = Review()

        # Assert that Review is a subclass of BaseModel
        self.assertTrue(issubclass(type(review), BaseModel))
    
    def test_review_string_representation(self):
        """
        Tests the string representation of Review.
        """
        # Create a new Review instance
        review = Review()

        # Assert that the string representation of Review is correct
        self.assertEqual(str(review), f"[Review] ({review.id}) {review.__dict__}")
    
    def test_review_to_dict(self):
        """
        Tests the to_dict method of Review.
        """
        # Create a new Review instance
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "This place is great!"

        # Get the dictionary representation of the Review instance
        review_dict = review.to_dict()

        # Assert that the dictionary is of type dict
        self.assertEqual(type(review_dict), dict)
        # Assert that the dictionary has the correct attribute values
        self.assertEqual(review_dict["place_id"], "123")
        self.assertEqual(review_dict["user_id"], "456")
        self.assertEqual(review_dict["text"], "This place is great!")

    def test_review_save(self):
        """
        Tests the save method of Review.
        """
        # Create a new Review instance
        review = Review()

        # Save the Review instance
        review.save()

        # Get all objects in storage
        all_objects = storage.all()

        # Assert that the Review instance is in storage
        self.assertIn(review, all_objects.values())


if __name__ == "__main__":
    unittest.main()