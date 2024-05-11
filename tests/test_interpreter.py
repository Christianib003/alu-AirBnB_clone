#! /usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO

from console import Interpreter

class TestInterpreter(unittest.TestCase):
    """Test the console interpreter"""
    
    def setUp(self):
        """Create a new Interpreter instance before each test case"""
        self.interpreter = Interpreter()

    def test_emptyline(self):
        """Test that emptyline method shifts the cursor to new line"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.interpreter.emptyline()
            self.assertEqual(fake_out.getvalue(), "")
    
    def test_quit(self):
        """Test that the do_quit method stops the program console"""
        self.assertTrue(self.interpreter.do_quit("quit"))


if __name__ == "__main__":
    unittest.main()