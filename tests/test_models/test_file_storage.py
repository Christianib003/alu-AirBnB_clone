#! /usr/bin/python3

import unittest
import os
import json

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
        """
        Clean up method that is called after each test case.
        Removes the test file created during the test case execution.
        """
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
    
    def test_save(self):
        """
        Test the save method of the FileStorage class.

        This method creates a new instance of the BaseModel class, sets its id to '1',
        adds it to the storage, saves the storage to a file, and then checks if the data
        in the file matches the expected data.
        """
        my_obj = BaseModel()
        my_obj.id = '1'
        self.storage.new(my_obj)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, "r") as f:
            data = json.load(f)
        self.assertEqual(data, {'BaseModel.1': my_obj.to_dict()})

    def test_save_with_multiple_objects(self):
            """
            Test case to verify the behavior of the save method when multiple objects are saved.

            This test case creates two instances of the BaseModel class, sets the id attribute of each instance,
            adds the instances to the storage, saves the storage, opens the file and loads the data, and asserts
            that the loaded data matches the expected dictionary.
            """
            obj1 = BaseModel()
            obj1.id = '1'
            obj2 = BaseModel()
            obj2.id = '2'
            self.storage.new(obj1)
            self.storage.new(obj2)
            self.storage.save()
            with open(self.storage._FileStorage__file_path, "r") as f:
                data = json.load(f)
            self.assertEqual(data, {'BaseModel.1': obj1.to_dict(), 'BaseModel.2': obj2.to_dict()})


if __name__ == '__main__':
    unittest.main()