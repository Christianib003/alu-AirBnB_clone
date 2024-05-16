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
    
    def test_city_inherits_from_basemodel(self):
        """
        Tests that City inherits from BaseModel.
        """
        # Create a new City instance
        city = City()

        # Assert that City is a subclass of BaseModel
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_city_string_representation(self):
        """
        Tests the string representation of City.
        """
        # Create a new City instance
        city = City()

        # Assert that the string representation of City is correct
        self.assertEqual(str(city), f"[City] ({city.id}) {city.__dict__}")

    def test_city_to_dict(self):
        """
        Tests the to_dict method of City.
        """
        # Create a new City instance
        city = City()

        # Add values to City's class attributes
        city.state_id = "123"
        city.name = "Michigan"

        # Get the dictionary representation of City
        city_dict = city.to_dict()

        # Assert that the dictionary representation has the correct keys
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("__class__", city_dict)
        self.assertIn("state_id", city_dict)
        self.assertIn("name", city_dict)

if __name__ == "__main__":
    unittest.main()