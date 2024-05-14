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
        self.assertIsInstance(self.base_model_instance.id, str)

        # Test if created_at and updated_at are datetime objects
        self.assertIsInstance(self.base_model_instance.created_at, datetime)
        self.assertIsInstance(self.base_model_instance.updated_at, datetime)

        # Test if the attributes are correctly set when kwargs is not empty
        kwargs = {
            "id": "123",
            "created_at": "2024-05-14T08:25:00.000000",
            "updated_at": "2024-05-14T08:25:00.000000",
            "__class__": "BaseModel" # should not be used when creating an instance
        }
        model_with_kwargs = BaseModel(**kwargs)
        self.assertEqual(model_with_kwargs.id, "123")
        self.assertEqual(model_with_kwargs.created_at, datetime.strptime("2024-05-14T08:25:00.000000", "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(model_with_kwargs.updated_at, datetime.strptime("2024-05-14T08:25:00.000000", "%Y-%m-%dT%H:%M:%S.%f"))
    
    def test_save(self):
        """Test if save method updates the updated_at attr  ibute"""
        # Save the model
        updated_at = self.base_model_instance.save()

        # Test if the updated_at attribute is updated
        self.assertEqual(updated_at, self.base_model_instance.updated_at) 
    
    def test_to_dict(self):
        """Test if the to_dict method returns the correct dictionary version of the instance"""
        # Convert the model to a dictionary
        model_inst_dict = self.base_model_instance.to_dict()

        # Test if __class__ key is in the dictionary
        self.assertIn("__class__", model_inst_dict)

        # Test if the __class__ key value is the model class name
        self.assertEqual(model_inst_dict["__class__"], self.base_model_instance.__class__.__name__)

        # Check if created_at and updated_at are in ISO format
        self.assertEqual(model_inst_dict["created_at"], self.base_model_instance.created_at.isoformat())
        self.assertEqual(model_inst_dict["updated_at"], self.base_model_instance.updated_at.isoformat())
    
    def test_str(self):
        """Test if the __str__ method returns the correct string representation of the instance"""
        expected_str = f"[{self.base_model_instance.__class__.__name__}] ({self.base_model_instance.id}) {self.base_model_instance.__dict__}"
        self.assertEqual(str(self.base_model_instance), expected_str)
    

if __name__ == "__main__":
    unittest.main()
