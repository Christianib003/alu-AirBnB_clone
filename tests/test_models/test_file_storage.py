#! /usr/bin/python3

import unittest
import os

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
    This class contains unit tests for the FileStorage class.
    """

    def setUp(self):
        """
        This method is called before each test case to set up
        any necessary dependencies.
        """
        self.storage = FileStorage()
        self.test_file = "test_file.json"
        self.storage._FileStorage__file_path = self.test_file

    def tearDown(self):
        """Clean up test effects."""
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass
    
    def test_all_with_no_objects(self):
        """
        This test case checks if the `all` method returns an empty dictionary
        when no objects were created beforehand.
        """
        self.assertEqual(self.storage.all(), {})

    def test_new_with_valid_object(self):
        """
        This test case checks if the 'new' method of the storage object correctly
        adds a new object to the storage.
        """
        my_obj = BaseModel()
        my_obj.id = "1" # override the attribute 'id' with a simple value
        self.storage.new(my_obj)
        self.assertIn("BaseModel.1", self.storage.all())

    def test_new_with_no_id(self):
        """
        This test case checks if the `new` method raises an `AttributeError`when
        trying to create a new object without an id.
        """
        obj = type('obj', (object,), {})
        with self.assertRaises(AttributeError):
            self.storage.new(obj)
    
    def test_new_with_same_id(self):
        """
        Test case to verify that the `new` method correctly handles
        objects with the same id.

        It creates two instances of the BaseModel class with the same id and adds
        them to the storage. Then it checks if the storage contains only the second
        object added, as the first one should be overwritten due to having the same id.
        """
        obj1 = BaseModel()
        obj1.id = '1'
        obj2 = BaseModel()
        obj2.id = '1'
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.assertEqual(self.storage.all(), {'BaseModel.1': obj2})


if __name__ == '__main__':
    unittest.main()