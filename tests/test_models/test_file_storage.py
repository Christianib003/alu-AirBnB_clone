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


if __name__ == '__main__':
    unittest.main()