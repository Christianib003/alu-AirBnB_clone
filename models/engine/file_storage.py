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
        """
        Adds a new object to the storage system.

        Args:
            obj: The object to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves all objects in the storage system to a JSON file.
        """
        all_objects = FileStorage.__objects
        obj_dict = {}
        for key, value in all_objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        pass
        