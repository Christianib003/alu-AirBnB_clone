#! /usr/bin/python3

import uuid

from datetime import datetime
import models


class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialize the Base model with three instance attributes"""
        
        self.id = str(uuid.uuid4()) # It's a requirement to convert id to string
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # Convert the datetime string to datetime object
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            
        models.storage.new(self)
    
    def save(self):
        """Updates the updated_at attribute to the current datetime when the object is updated"""
        self.updated_at = datetime.now()
        models.storage.save()
        return self.updated_at # return the updated "updated_at" attribute
    
    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        instance_dict = self.__dict__.copy() # Use copy() to avoid modifying the original dictionary
        instance_dict["__class__"] = self.__class__.__name__

        # Convert the datetime objects to ISO format
        # isoformat() -> %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
    
    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
