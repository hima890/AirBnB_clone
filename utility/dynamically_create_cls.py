#!/usr/bin/python3
"""
Dynamically Create classes
"""
from models.base_model import BaseModel


def dynamicallyCreateCls(className):
    try:
        # Dynamically get the class using globals() and getattr()
        cls = globals()[className]

        # Create a new class instance
        new_instance = cls()

        # Save the instance (assuming save() method exists in the class)
        new_instance.save()

        # Print the instance id (assuming id attribute exists in the instance)
        print(new_instance.id)

    except KeyError:
        print("** class doesn't exist **")
        return None  # Return None to indicate failure

    except Exception as e:
        print(e)  # Print any other exception that might occur
        return None  # Return None to indicate failure
