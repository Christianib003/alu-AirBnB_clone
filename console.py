#! /usr/bin/python3

from cmd import Cmd

class Interpreter(Cmd):
    """This is a command line interpreter for interacting with the program"""
    
    prompt = "(hbnb) "

    def emptyline(self):
        """Shift cursor to new line when user enters an empty line"""
        pass

    def do_quit(self, input):
        """Handle quiting interpreter when user types 'quit' command"""
        return True
    
    def do_EOF(self, input):
        """Handle end-of-file condition. eg: user pressing 'ctrl + D'."""
        print()
        return True
    
    @classmethod
    def run_from_file(cls, filename):
        """Run commands from a file"""
        with open(filename, 'r') as file:
            interpreter = cls()
            for line in file:
                interpreter.onecmd(line)


if __name__ == "__main__":
    """Check if a file is provided as an argument and run commands from it"""
    import sys
    if len(sys.argv) > 1:
        Interpreter.run_from_file(sys.argv[1])
    else:
        interpreter = Interpreter()
        interpreter.cmdloop()