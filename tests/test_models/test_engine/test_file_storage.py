#! /usr/bin/python3

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
    
    def test_class_attributes(self):
        """
        Test the class attributes of FileStorage.
        """
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)


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

    def test_save(self):
        """
        Test the 'save' method of the FileStorage class.
        """
        # Save all objects currently stored in the instance to a file named 'file.json'.
        self.storage.save()

        # Check that the file 'file.json' is created.
        self.assertTrue(os.path.exists('file.json'))

        # Open the file 'file.json' and load its contents into a dictionary.
        with open('file.json', 'r') as f:
            obj_dict = json.load(f)

        # Check that the dictionary contains the BaseModel instance created in the setUp method.
        self.assertIn('BaseModel.' + self.obj.id, obj_dict)

        # Check that the 'id' attribute of the dictionary entry for this instance is the same as the 'id' of the instance.
        self.assertEqual(obj_dict['BaseModel.' + self.obj.id]['id'], self.obj.id)

    def test_reload(self):
        """
        Test the 'reload' method of the FileStorage class.
        """
        # Save all objects currently stored in the instance to a file named 'file.json'.
        self.storage.save()

        # Clear all objects currently stored in the instance.
        self.storage.reset()

        # Load all objects from the file back into the instance.
        self.storage.reload()

        # Get all objects currently stored in the instance.
        all_objects = self.storage.all()

        # Check that the dictionary contains the BaseModel instance created in the setUp method.
        self.assertIn('BaseModel.' + self.obj.id, all_objects)

        # Check that the 'id' attribute of the dictionary entry for this instance is the same as the 'id' of the instance.
        self.assertEqual(all_objects['BaseModel.' + self.obj.id].id, self.obj.id)


if __name__ == '__main__':
    unittest.main()