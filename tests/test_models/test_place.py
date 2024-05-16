#! /usr/bin/python3

import unittest
import os

from models import storage
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Unit test class for Place
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
    
    def test_place_attributes(self):
        """
        Tests the default values of Place attributes.
        """
        # Create a new Place instance
        place = Place()

        # Assert that city_id, user_id, name, and description are empty strings
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

if __name__ == "__main__":
    unittest.main()