#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""


import cmd
from models import storage
from utility.dynamically_create_cls import dynamicallyCreateCls

""""
console.py
    This class represents the command interpreter, and the control center
    of this project. It defines function handlers for all commands inputted
    in the console and calls the appropriate storage engine APIs to manipulate
    application data / models.
"""


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    # All the supported classes that globals function used
    __supported_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        Usage: create <class name>
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return None

        if len(args) != 1:
            print("** expicted one arguminte **")
            return None

        className = args[0]
        print(type(className))
        if className not in HBNBCommand.__supported_classes:
            print("** class doesn't exist **")
            return None

        dynamicallyCreateCls(className)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return None

        className = args[0]
        if className not in HBNBCommand.__supported_classes:
            print("** class doesn't exist **")
            return None

        if len(args) != 2:
            print("** instance id missing **")
            return None

        classId = args[1]
        key = "{}.{}".format(className, classId)
        if key not in storage.all().keys():
            print("** no instance found **")
            return None

        instance = storage.all()[key]
        print("{}".format(instance))

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return None

        className = args[0]
        if className not in HBNBCommand.__supported_classes:
            print("** class doesn't exist **")
            return None

        if len(args) != 2:
            print("** instance id missing **")
            return None

        classId = args[1]
        key = "{}.{}".format(className, classId)
        if key not in storage.all().keys():
            print("** no instance found **")
            return None

        storage.delete(key)

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name."""
        args = arg.split()
        all_objs = storage.all()
        result = []

        if not args:
            # No class name provided, print all instances
            for obj in all_objs.values():
                result.append(str(obj))
        else:
            class_name = args[0]
            if class_name not in self.__supported_classes:
                print("** class doesn't exist **")
                return None
            # Print all instances of the specified class
            for key, obj in all_objs.items():
                if key.startswith(class_name + "."):
                    result.append(str(obj))

        print(result)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__supported_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3].strip('"')

        # Cast attribute value to the correct type
        instance = all_objs[key]
        # Default to str if attribute doesn't exist
        attr_type = type(getattr(instance, attr_name, str))
        try:
            if attr_type == int:
                attr_value = int(attr_value)
            elif attr_type == float:
                attr_value = float(attr_value)
            else:
                attr_value = str(attr_value)
        except ValueError:
            print("** value type error **")
            return

        setattr(instance, attr_name, attr_value)
        instance.save()

    def do_help(self, arg):

        """To get help on a command, type help <topic>.
        """
        return super().do_help(arg)

    def do_EOF(self, line):
        """Inbuilt EOF command to gracefully catch errors.
        """
        print("")
        return True

    def emptyline(self):
        """Override default `empty line + return` behaviour.
        """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program.
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
