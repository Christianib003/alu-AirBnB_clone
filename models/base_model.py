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