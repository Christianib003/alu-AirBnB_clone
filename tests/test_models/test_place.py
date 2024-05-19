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
    
    def test_place_inherits_from_basemodel(self):
        """
        Tests that Place inherits from BaseModel.
        """
        # Create a new Place instance
        place = Place()

        # Assert that Place is a subclass of BaseModel
        self.assertTrue(issubclass(type(place), BaseModel))
    
    def test_place_to_dict(self):
        """
        Tests the to_dict method of Place.
        """
        # Create a new Place instance
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Far away from home"
        place.description = "No tenant needed"
        place.number_rooms = 1
        place.number_bathrooms = 1
        place.max_guest = 1
        place.price_by_night = 1
        place.latitude = 1.0
        place.longitude = 1.0
        place.amenity_ids = ["amenity_id1"]

        # Get the dictionary representation of Place
        place_dict = place.to_dict()

        # Assert that the dictionary is formatted correctly
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["id"], place.id)
        self.assertEqual(place_dict["created_at"], place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"], place.updated_at.isoformat())
        self.assertEqual(place_dict["city_id"], place.city_id)
        self.assertEqual(place_dict["user_id"], place.user_id)
        self.assertEqual(place_dict["name"], place.name)
        self.assertEqual(place_dict["description"], place.description)
        self.assertEqual(place_dict["number_rooms"], place.number_rooms)
        self.assertEqual(place_dict["number_bathrooms"], place.number_bathrooms)
        self.assertEqual(place_dict["max_guest"], place.max_guest)
        self.assertEqual(place_dict["price_by_night"], place.price_by_night)
        self.assertEqual(place_dict["latitude"], place.latitude)
        self.assertEqual(place_dict["longitude"], place.longitude)
        self.assertEqual(place_dict["amenity_ids"], place.amenity_ids)
    
    def test_place_string_representation(self):
        """
        Tests the string representation of Place.
        """
        # Create a new Place instance
        place = Place()

        # Get the string representation of Place
        place_str = str(place)

        # Assert that the string representation is formatted correctly
        self.assertEqual(place_str, f"[Place] ({place.id}) {place.__dict__}")
    
    def test_place_save(self):
        """
        Tests the save method of Place.
        """
        # Create a new Place instance
        place = Place()

        # Save the place
        place.save()

        # Assert that the place was added to the storage
        self.assertIn(f"Place.{place.id}", storage.all())


if __name__ == "__main__":
    unittest.main()