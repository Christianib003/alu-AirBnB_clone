#! /usr/bin/python3
"""This module contains the command line interpreter for the program"""

import cmd
import shlex

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """This is a command line interpreter for interacting with the program"""
    
    prompt = "(hbnb) "

    # Define classes which can be created using the "create" command
    valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

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
    
    def do_all(self, input):
        """Prints all string representation of all instances based or not on the class name.

        Args:
            input (str): The input string containing the class name.

        Returns:
            None
        """
        args = shlex.split(input)

        # if no class name is provided, print all instances
        if len(args) == 0:
            objects = storage.all()
            print([str(obj) for obj in objects.values()])
        
        # if an invalid class name is provided, notify user
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        
        # if a valid class name is provided, print all instances of that class
        else:
            objects = storage.all()
            for key, value in objects.items():
                if key.split(".")[0] == args[0]:
                    print(str(value))
    
    def do_update(self, input):
        """Updates an instance based on the class name and id by adding or updating attribute.

        Args:
            input (str): The input string containing the class name, instance id, attribute name, and attribute value.

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
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            # Get all currently stored objects
            objects = storage.all()

            # Construct a key in format "<class name>.<id>"
            key = args[0] + "." + args[1]

            # Update the object if key exists in objects
            if key in objects:
                obj = objects[key]
                setattr(obj, args[2], args[3])
                obj.save()
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
    HBNBCommand().cmdloop()
    # import sys
    # if len(sys.argv) > 1:
    #     HBNBCommand.run_from_file(sys.argv[1])
    # else:
    #     interpreter = HBNBCommand()
    #     interpreter.cmdloop()