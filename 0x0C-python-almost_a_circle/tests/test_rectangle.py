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
        rect = Rectangle(7, 14)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 14)

    def test_negative_width(self):
        self.assertRaisesRegex(ValueError, "width must be > 0", Rectangle, -3, 6)

    def test_negative_height(self):
        self.assertRaisesRegex(ValueError, "height must be > 0", Rectangle, 7, -5)

    def test_zero_width(self):
        self.assertRaisesRegex(ValueError, "width must be > 0", Rectangle, 0, 10)

    def test_zero_height(self):
        self.assertRaisesRegex(ValueError, "height must be > 0", Rectangle, 15, 0)

    def test_negative_x(self):
        self.assertRaisesRegex(ValueError, "x must be >= 0", Rectangle, 2, 6, -4)

    def test_negative_y(self):
        self.assertRaisesRegex(ValueError, "y must be >= 0", Rectangle, 2, 6, 4, -7)

    def test_string_width(self):
        self.assertRaisesRegex(TypeError, "width must be an integer", Rectangle, "3", 6)

    def test_string_height(self):
        self.assertRaisesRegex(TypeError, "height must be an integer", Rectangle, 12, "16")

    def test_string_x(self):
        self.assertRaisesRegex(TypeError, "x must be an integer", Rectangle, 12, 16, "3")

    def test_string_y(self):
        self.assertRaisesRegex(TypeError, "y must be an integer", Rectangle, 12, 16, 3, "5")

    def test_all_positive(self):
        rect = Rectangle(7, 14, 3, 9,30)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 14)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 9)
        self.assertEqual(rect.id, 30)
        
    def test_area(self):
        rect = Rectangle(6, 7)
        self.assertEqual(rect.area(), 42)
