import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """
    This class contains the test cases for the FileStorage class.
    """
    def setUp(self):
        """
        This method Sets up the testing dependencies before each test case
        """
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.storage.new(self.obj)

    def tearDown(self):
        """
        This method cleans up the testing dependencies after each test case
        """
        del self.storage
        del self.obj
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_all(self):
        """
        Test the 'all' method of the FileStorage class.
        """
        # Call the 'all' on storage to return a dictionary of all objects 
        # currently stored in the instance.
        all_objects = self.storage.all()

        # Check that the dictionary contains the BaseModel instance created in the setUp method.
        self.assertIn('BaseModel.' + self.obj.id, all_objects)

        # Check that the value associated with this key is the same BaseModel instance.
        self.assertEqual(all_objects['BaseModel.' + self.obj.id], self.obj)

    def test_new(self):
        """
        Test the 'new' method of the FileStorage class.
        """
        obj2 = BaseModel()
        self.storage.new(obj2)
        all_objects = self.storage.all()

        # Check that the dictionary contains the new BaseModel instance.
        self.assertIn('BaseModel.' + obj2.id, all_objects)

        # Check that the value associated with this key is the new BaseModel instance.
        self.assertEqual(all_objects['BaseModel.' + obj2.id], obj2)


if __name__ == '__main__':
    unittest.main()