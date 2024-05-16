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

if __name__ == "__main__":
    unittest.main()