import unittest
import os

from models import storage
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unit test class for User model"""

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

    def test_user_attributes(self):
        """
        Tests the default values of User attributes.
        """
        # Create a new User instance
        user = User()

        # Assert that email, password, first_name, and last_name are empty strings
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
