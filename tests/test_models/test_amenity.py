#! /usr/bin/python3

import unittest
import os

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Unit test class for Amenity"""

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
    
    def test_amenity_attributes(self):
        """
        Tests the default values of Amenity attributes.
        """
        # Create a new Amenity instance
        amenity = Amenity()

        # Assert that name is an empty string
        self.assertEqual(amenity.name, "")
    
    def test_amenity_inherits_from_basemodel(self):
        """
        Tests that Amenity inherits from BaseModel.
        """
        # Create a new Amenity instance
        amenity = Amenity()

        # Assert that Amenity is a subclass of BaseModel
        self.assertTrue(issubclass(type(amenity), BaseModel))
    
    def test_amenity_string_representation(self):
        """
        Tests the string representation of Amenity.
        """
        # Create a new Amenity instance
        amenity = Amenity()

        # Assert that the string representation of Amenity is correct
        self.assertEqual(str(amenity), f"[Amenity] ({amenity.id}) {amenity.__dict__}")

if __name__ == "__main__":
    unittest.main()