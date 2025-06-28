#!/usr/bin/python3
""" test base module """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os

class TestBase(unittest.TestCase):
    """
    test base class
    """
    def tearDown(self):
        """Delete created files after each test."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_create_first_object(self):
        first_object = Base()
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_new_id(self):
        new_id = Base(25)
        self.assertEqual(new_id.id, 25)

    def test_to_json_string(self):
        pass



if __name__ == "__main__":
    unittest.main(verbosity=2)
