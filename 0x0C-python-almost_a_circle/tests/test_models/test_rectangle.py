#!/usr/bin/python3
"""base test module"""


import unittest
from model.rectangle import Rectangle
"""import things"""


class TestBase(unittest.TestCase):
    """test base class cases"""
    
    def 5-display(self):
        """
        Test display method
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 4)
        result1 = "##\n" \
                  "##\n" \
                  "##\n" \
                  "##\n"
        r2 = Rectangle(2, 3)
        result2 = "##\n" \
                  "##\n" \
                  "##\n"
        r3 = Rectangle(1, 1)
        result3 = "#\n" \
                  try:
        r1.display()
        self.assertEqual(sys.stdout.getvalue(), result1)
    finally:
        sys.stdout.seek(0)
        sys.stdout.truncate(0)
        try:
            r2.display()
            self.assertEqual(sys.stdout.getvalue(), result2)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
            try:
                r3.display()
                self.assertEqual(sys.stdout.getvalue(), result3)
            finally:
                sys.stdout.seek(0)
                sys.stdout.truncate(0)
