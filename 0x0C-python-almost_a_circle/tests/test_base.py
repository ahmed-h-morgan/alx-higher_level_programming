#!/usr/bin/python3
""" test base module """


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    test base class
    """
    def test_create_first_object(self):
        first_object = Base()
        self.assertEqual(Base._Base__nb_objects, 1)
