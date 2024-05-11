#! /usr/bin/python3

from cmd import Cmd

class Interpreter(Cmd):
    """This is a command line interpreter for interacting with the program"""
    pass


if __name__ == "__main__":
    """Continuously prompt the user for input"""
    Interpreter.cmdloop()