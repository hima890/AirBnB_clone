#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

""""
console.py
    This class represents the command interpreter, and the control center
    of this project. It defines function handlers for all commands inputted
    in the console and calls the appropriate storage engine APIs to manipulate
    application data / models.
"""


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
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
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        if len(args) != 1:
            print("** expicted one arguminte **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.__supported_classes:
            print("** class doesn't exist **")
            return

        try:
            # Dynamically get the class using globals() and getattr()
            cls = globals()[class_name]
            # Create a new class instance
            new_instance = cls()
            # Save the instance
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")
        except Exception as e:
            print(e)

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
