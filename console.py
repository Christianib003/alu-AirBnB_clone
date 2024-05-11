#! /usr/bin/python3
import sys
from cmd import Cmd

class Interpreter(Cmd):
    """This is a command line interpreter for interacting with the program"""
    
    def do_quit(self, input):
        """handles the quiting of the application when user types <quit>"""
        sys.exit()


if __name__ == "__main__":
    """Continuously prompt the user for input"""
    interpreter = Interpreter()
    interpreter.cmdloop()