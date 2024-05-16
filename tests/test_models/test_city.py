#! /usr/bin/python3

import unittest
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

if __name__ == "__main__":
    unittest.main()