#! /usr/bin/python3

import unittest
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    def setUp(self):
        """Set up BaseModel instance for testing"""
        self.base_model_instance = BaseModel()
    
    def tearDown(self):
        """Clean up BaseModel instance after testing"""
        del self.base_model_instance
    
    def test_init(self):
        """Test BaseModel instance initialization"""
        # Test if the attributes are set after initialization
        self.assertIsNotNone(self.base_model_instance.id)
        self.assertIsNotNone(self.base_model_instance.created_at)
        self.assertIsNotNone(self.base_model_instance.updated_at)

        # Test if the id is a string
        self.assertIsInstance(self.model.id, str)

        # Test if created_at and updated_at are datetime objects
        self.assertIsInstance(self.base_model_instance.created_at, datetime)
        self.assertIsInstance(self.base_model_instance.updated_at, datetime)
    

if __name__ == "__main__":
    unittest.main()