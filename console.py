#! /usr/bin/python3
"""This module contains the command line interpreter for the program"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """This is a command line interpreter for interacting with the program"""
    
    prompt = "(hbnb) "

    # Define classes which can be created using the "create" command
    valid_classes = ["BaseModel"]

    def do_create(self, input):
        """Create a new instance of a class"""
        args = shlex.split(input)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
    
    def do_show(self, input):
        """Prints the string representation of an instance.

        Args:
            input (str): The input string containing the class name and instance id.

        Returns:
            None
        """
        args = shlex.split(input)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            # Get all currently stored objects
            objects = storage.all()

            # Construct a key in format "<class name>.<id>"
            key = args[0] + "." + args[1]

            # Check if key exists in objects
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
    
    def do_destroy(self, input):
        """Deletes an instance based on the class name and id.

        Args:
            input (str): The input string containing the class name and instance id.

        Returns:
            None
        """
        args = shlex.split(input)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            # Get all currently stored objects
            objects = storage.all()

            # Construct a key in format "<class name>.<id>"
            key = args[0] + "." + args[1]

            # Check if key exists in objects
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

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
    
    def help(self):
        """Display help message"""
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit")
    
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
        HBNBCommand.run_from_file(sys.argv[1])
    else:
        interpreter = HBNBCommand()
        interpreter.cmdloop()