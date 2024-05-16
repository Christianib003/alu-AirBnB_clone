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

    def test_amenity_save(self):
        """
        Tests the save method of Amenity.
        """
        # Create a new Amenity instance
        amenity = Amenity()

        # Save the Amenity
        amenity.save()

        # Get all stored objects
        objects = storage.all()

        # Construct the key
        key = f"{amenity.__class__.__name__}.{amenity.id}"

        # Check if the key exists in objects
        self.assertTrue(key in objects)
    
    def test_amenity_to_dict(self):
        """
        Tests the to_dict method of Amenity.
        """
        # Create a new Amenity instance
        amenity = Amenity()

        # Set attributes for Amenity
        amenity.name = "Wifi"

        # Convert Amenity to dictionary
        amenity_dict = amenity.to_dict()

        # Assert that the dictionary is formatted correctly
        self.assertEqual(amenity_dict, {
            "id": amenity.id,
            "created_at": amenity.created_at.isoformat(),
            "updated_at": amenity.updated_at.isoformat(),
            "name": "Wifi",
            "__class__": "Amenity"
        })
    
if __name__ == "__main__":
    unittest.main()