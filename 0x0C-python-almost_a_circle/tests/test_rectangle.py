#!/usr/bin/python3
""" Test Rectangle module """


import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    Test Rectangle class
    """
    def test_only_width(self):
        """ only width argument """
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_positive_width_and_height(self):
        """ only positive width and height """
        Rectangle(10,4)

    def test_negative_width(self):
        pass