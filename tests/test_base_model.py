#! /usr/bin/python3

import unittest
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    def setUp(self):
        """Set up BaseModel instance for testing"""
        self.base_model_instance = BaseModel()
    

if __name__ == "__main__":
    unittest.main()