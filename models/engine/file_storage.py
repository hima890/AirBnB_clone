#!/usr/bin/python3

import json



"""
Module: for FileStorage class
define a class named FileStorage
"""

class FileStorage:
    """
        This class serializes instances to a JSON file and
        deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Returns the dictionary __objects
        """
        return FileStorage.__objects
    def new(self, obj):
        """
            Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
    def reload(self):
        """
        Deserializes the JSON file to __objects if the file exists.
        If the file doesn't exist, do nothing.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    # Assuming you have a method from_dict() in each class to recreate objects from dictionaries
                    obj = globals()[class_name].from_dict(obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass  # If the file doesn't exist, do nothing
        
