#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
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

    __file_path = "models/engine/file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """

        return self.__objects

    def new(self, obj):

        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects if the file exists.
        If the file doesn't exist, do nothing.
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    print("BaseModel" in globals())
                    obj = globals()[class_name].from_dict(obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass  # If the file doesn't exist, do nothing
