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
        print("\n")
        return True


def run_from_file(filename):
    """Run commands from a file"""
    with open(filename, 'r') as file:
        interpreter = Interpreter()
        for line in file:
            interpreter.onecmd(line)

