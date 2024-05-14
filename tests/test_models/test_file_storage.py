#! /usr/bin/python3

import unittest

from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""
    
    def setUp(self):
        """Setup test dependencies."""
        self.storage = FileStorage()
        self.test_file = "test_file.json"
        self.storage._FileStorage__file_path = self.test_file

if __name__ == '__main__':
    unittest.main()