#! /usr/bin/python3

import unittest
from console import Interpreter

class TestInterpreter(unittest.TestCase):
    """Test the console interpreter"""
    
    def setUp(self):
        """Create a new Interpreter instance before each test case"""
        self.interpreter = Interpreter()


if __name__ == "__main__":
    unittest.main()