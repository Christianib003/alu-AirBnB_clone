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

    def __init__(self):
        # create the file if it doesn't exist
        if not os.path.exists(self.__file_path):
            with open(self.__file_path, 'w') as f:
                json.dump({}, f)

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
        """
        Loads objects from a JSON file into the storage system.
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    cls = eval(class_name)
                    inst = cls(**value)
                    FileStorage.__objects[key] = inst
        except:
            pass
    
    # For testing purposes only
    def reset(self):
        """
        Resets the storage system by clearing all objects.
        """
        self._FileStorage__objects = {}
        