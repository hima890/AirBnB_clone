#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
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