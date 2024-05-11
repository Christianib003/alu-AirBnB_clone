#! /usr/bin/python3

from cmd import Cmd

class Interpreter(Cmd):
    """This is a command line interpreter for interacting with the program"""
    
    def do_quit(self, input):
        """handle the quiting of the interpreter when user types 'quit' command"""
        return True

    
if __name__ == "__main__":
    """Continuously prompt the user for input"""
    interpreter = Interpreter()
    interpreter.cmdloop()