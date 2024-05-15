#! /usr/bin/python3

import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    This class represents a file storage system for storing and retrieving objects in JSON format.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects currently stored.
        """
        return FileStorage.__objects

    def new(self, obj):
        pass

    def save(self):
        pass

    def reload(self):
        pass
