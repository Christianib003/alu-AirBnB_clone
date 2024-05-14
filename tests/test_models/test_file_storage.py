#! /usr/bin/python3

import unittest
import os

from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""

    def setUp(self):
        """Setup test dependencies."""
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
        """Test the all method with no objects."""
        self.assertEqual(self.storage.all(), {})

    def test_new_with_valid_object(self):
        """Test the new method with a valid object"""
        obj = type('obj', (object,), {'id': '1'})
        self.storage.new(obj)
        self.assertIn('obj.1', self.storage.all())
    
    def test_new_with_no_id(self):
        """Test the new method with an object without an id"""
        obj = type('obj', (object,), {})
        with self.assertRaises(AttributeError):
            self.storage.new(obj)


if __name__ == '__main__':
    unittest.main()