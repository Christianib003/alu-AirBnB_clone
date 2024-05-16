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
    
    def test_state_attributes(self):
        """
        Tests the default values of State attributes.
        """
        # Create a new State instance
        state = State()

        # Assert that name is an empty string
        self.assertEqual(state.name, "")

    def test_state_inherits_from_basemodel(self):
        """
        Tests that State inherits from BaseModel.
        """
        # Create a new State instance
        state = State()

        # Assert that State is a subclass of BaseModel
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_state_string_representation(self):
        """
        Tests the string representation of State.
        """
        # Create a new State instance
        state = State()

        # Add the name of the state
        state.name = "Michigan"

        # Assert that the string representation of State is correct
        self.assertEqual(str(state), f"[State] ({state.id}) {state.__dict__}")

    def test_state_to_dict(self):
        """
        Tests the to_dict method of State.
        """
        # Create a new State instance
        state = State()

        # Add the name of the state
        state.name = "Michigan"

        # Get the dictionary representation of the State instance
        state_dict = state.to_dict()

        # Assert that the dictionary representation has the correct class key
        self.assertEqual(state_dict["__class__"], "State")

        # Assert that the dictionary representation has the correct attributes
        self.assertEqual(state_dict["id"], state.id)
        self.assertEqual(state_dict["created_at"], state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"], state.updated_at.isoformat())
        self.assertEqual(state_dict["name"], state.name)


if __name__ == "__main__":
    unittest.main()