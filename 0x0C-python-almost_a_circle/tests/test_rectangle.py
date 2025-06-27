#!/usr/bin/python3
""" Test Rectangle module """


import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch

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

    def test_str(self):
        rect = Rectangle(7, 14, 3, 9,30)
        self.assertMultiLineEqual(rect.__str__(), "[Rectangle] (30) 3/9 - 7/14")

    def test_display_with_position(self):
        """Test display with x and y positions"""
        r1 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_x_only(self):
        """Test display with x position only (y=0)"""
        r2 = Rectangle(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r2.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_no_position(self):
        """Test display with no x and y positions (x=0, y=0)"""
        r3 = Rectangle(4, 2)
        expected_output = "####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r3.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_single_line(self):
        """Test display for a single line rectangle"""
        r4 = Rectangle(5, 1, 0, 3)
        expected_output = "\n\n\n#####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r4.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_no_arguments_passed(self):
        self.assertRaises(TypeError, Rectangle)

    def test_update_no_arguments(self):
        rect = Rectangle(1,1)
        rect.update()
        self.assertEqual(rect.id, 16)

    def test_update_one_argument(self):
        rect = Rectangle(1,1)
        rect.update(5)
        self.assertEqual(rect.id, 5)

    def test_to_dictionary(self):
        rect = Rectangle(10, 5, 2, 3, 1)
        expected_dict = {
            'id': 1,
            'width': 10,
            'height': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(rect.to_dictionary(), expected_dict)
