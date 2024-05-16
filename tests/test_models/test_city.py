#! /usr/bin/python3

import unittest
import os
from models import storage
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ 
    Unit test class for City model
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
    
    def test_city_attributes(self):
        """
        Tests the default values of City attributes.
        """
        # Create a new City instance
        city = City()

        # Assert that state_id and name are empty strings
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
    
    

if __name__ == "__main__":
    unittest.main()