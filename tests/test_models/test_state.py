#! /usr/bin/python3
import unittest
import os

from models import storage
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Unit test class for State model
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
    
    
if __name__ == "__main__":
    unittest.main()