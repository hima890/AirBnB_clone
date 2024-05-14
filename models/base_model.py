#!/usr/bin/python3
"""
This module provides a base model class for other classes.

It includes attributes and methods common to all models.
"""

import datetime
import uuid


class BaseModel:
    """
    This class serves as a base model for other classes.

    It provides attributes and methods common to all models.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        Attributes:
            id (str): A unique identifier generated using UUID.
            created_at (str): A string representation of the
            creation timestamp.
            updated_at (str): A string representation of the
            last update timestamp.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def save(self):
        """
        Updates the 'updated_at' attribute with the current timestamp.
        """
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """
        Converts the object to a dictionary.

        Returns:
            dict: A dictionary representation of the object.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string containing the class name, ID, and attributes.
        """
        return "[{}] /({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )
