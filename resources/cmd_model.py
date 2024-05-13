import cmd

class MyCmd(cmd.Cmd):
    """Simple command processor example."""
    
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
        print("")
        return True
    def default(self, line):
        print(f"Undefined command: {line}")
    
if __name__ == '__main__':
    MyCmd().cmdloop()
