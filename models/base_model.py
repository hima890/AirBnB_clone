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

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            id (str): A unique identifier generated using UUID.
            created_at (datetime): A datetime object representing
            the creation timestamp.
            updated_at (datetime): A datetime object representing
            the last update timestamp.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            format = "%Y-%m-%dT%H:%M:%S.%f"
            if "created_at" in kwargs.keys():
                self.created_at = datetime.datetime.strptime(
                    kwargs['created_at'], format
                    )
            if 'updated_at' in kwargs.keys():
                self.updated_at = datetime.datetime.strptime(
                    kwargs['updated_at'], format
                    )

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
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string containing the class name, ID,
            and attributes.
        """
        return "[{}] /({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )
