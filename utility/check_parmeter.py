


def check_parmeter(args):
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