#!/usr/bin/python3
""" Test Square module """


import unittest
from models.square import Square
from io import StringIO
from unittest.mock import patch

class TestSquare(unittest.TestCase):
    """
    Test Square class
    """
    # def test_only_width(self):
    #     self.assertRaises(TypeError, Square, 5)

    def test_positive_width(self):
        squ = Square(7)
        self.assertEqual(squ.width, 7)
        # self.assertEqual(squ.height, 14)

    def test_negative_width(self):
        self.assertRaisesRegex(ValueError, "width must be > 0", Square, -3, 6)

    # def test_negative_height(self):
    #     self.assertRaisesRegex(ValueError, "height must be > 0", Square, 7, -5)

    def test_zero_width(self):
        self.assertRaisesRegex(ValueError, "width must be > 0", Square, 0, 10)

    # def test_zero_height(self):
    #     self.assertRaisesRegex(ValueError, "height must be > 0", Square, 15, 0)

    def test_negative_x(self):
        self.assertRaisesRegex(ValueError, "x must be >= 0", Square, 2, -4)

    def test_negative_y(self):
        self.assertRaisesRegex(ValueError, "y must be >= 0", Square, 2, 4, -7)

    def test_string_width(self):
        self.assertRaisesRegex(TypeError, "width must be an integer", Square, "3", 6)

    # def test_string_height(self):
    #     self.assertRaisesRegex(TypeError, "height must be an integer", Square, 12, "16")

    def test_string_x(self):
        self.assertRaisesRegex(TypeError, "x must be an integer", Square, 12, "3")

    def test_string_y(self):
        self.assertRaisesRegex(TypeError, "y must be an integer", Square, 12, 3, "5")

    def test_all_positive(self):
        squ = Square(7, 3, 9,30)
        self.assertEqual(squ.width, 7)
        self.assertEqual(squ.x, 3)
        self.assertEqual(squ.y, 9)
        self.assertEqual(squ.id, 30)
    
    @unittest.skip("check if this is a required method in Square class or not")    
    def test_area(self):
        squ = Square(6, 7)
        self.assertEqual(squ.area(), 42)

    def test_str(self):
        squ = Square(7, 3, 9,30)
        self.assertMultiLineEqual(squ.__str__(), "[Square] (30) 3/9 - 7")

    def test_display_with_position(self):
        """Test display with x and y positions"""
        s1 = Square(2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_x_only(self):
        """Test display with x position only (y=0)"""
        s2 = Square(3, 1, 0)
        expected_output = " ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s2.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_no_position(self):
        """Test display with no x and y positions (x=0, y=0)"""
        s3 = Square(4)
        expected_output = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s3.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_single_line(self):
        """Test display for a single line rectangle"""
        s4 = Square(1, 0, 3)
        expected_output = "\n\n\n#\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s4.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_no_arguments_passed(self):
        self.assertRaises(TypeError, Square)

    def test_update_no_arguments(self):
        squa = Square(1,1)
        squa.update()
        self.assertEqual(squa.id, 31)

    def test_update_one_argument(self):
        squa = Square(1,1)
        squa.update(5)
        self.assertEqual(squa.id, 5)