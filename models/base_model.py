#! /usr/bin/python3

import uuid

from datetime import datetime


class BaseModel:
    """Base class for all models"""

    def __init__(self):
        """Initialize the Base model with three instance attributes"""
        self.id = str(uuid.uuid4()) # It's a requirement to convert id to string
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        """Updates the updated_at attribute to the current datetime when the object is updated"""
        self.updated_at = datetime.now()
        return self.updated_at # return the updated "updated_at" attribute