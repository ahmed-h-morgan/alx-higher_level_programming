#!/usr/bin/python3
""" Test Rectangle module """


import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    Test Rectangle class
    """
    def test_only_width(self):
        self.assertRaises(TypeError, Rectangle, 5)

    def test_positive_width_and_height(self):
        rect = Rectangle(7,14)
        self.assertEqual(rect.width,7)
        self.assertEqual(rect.height, 14)

    def test_negative_width(self):
        pass