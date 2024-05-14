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

if __name__ == '__main__':
    unittest.main()