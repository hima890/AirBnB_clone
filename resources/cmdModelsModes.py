#!/usr/bin/python3

import cmd
import sys

class MyCmd(cmd.Cmd):
    """Simple command processor example."""

    prompt = '(Cmd) '

    def do_greet(self, person):
        """Greet the named person"""
        if person:
            print("Hello,", person)
        else:
            print('Hello')

    def help_greet(self):
        print("Syntax: greet [person]")
        print("Greet the named person")

    def do_EOF(self, line):
        """Exit the program"""
        return True

def run_interactive():
    MyCmd().cmdloop()

def run_non_interactive(arguments):
    cmd_instance = MyCmd()
    for arg in arguments:
        cmd_instance.onecmd(arg)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        run_non_interactive(sys.argv[1:])
    else:
        run_interactive()
