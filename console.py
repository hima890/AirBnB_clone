#!/usr/bin/python3
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
        args = arg.split()

        if not args:
            print("** class name missing **")
            return None

        if len(args) != 1:
            print("** expicted one arguminte **")
            return None

        className = args[0]
        if className not in HBNBCommand.__supported_classes:
            print("** class doesn't exist **")
            return None

        dynamicallyCreateCls(className)

    def do_show(self, arg):
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
