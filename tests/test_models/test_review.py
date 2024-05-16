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
    
    

if __name__ == "__main__":
    unittest.main()