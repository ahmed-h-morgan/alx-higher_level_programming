#!/usr/bin/python3
""" Test Square module """


import unittest
from models.square import Square
from io import StringIO
from unittest.mock import patch
from models.base import Base
import os

class TestSquare(unittest.TestCase):
    """
    Test Square class
    """
    def tearDown(self):
        """Delete created files after each test."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_positive_width(self):
        squ = Square(7)
        self.assertEqual(squ.width, 7)

    def test_negative_width(self):
        self.assertRaisesRegex(ValueError, "width must be > 0", Square, -3, 6)

    def test_zero_width(self):
        self.assertRaisesRegex(ValueError, "width must be > 0", Square, 0, 10)

    def test_negative_x(self):
        self.assertRaisesRegex(ValueError, "x must be >= 0", Square, 2, -4)

    def test_negative_y(self):
        self.assertRaisesRegex(ValueError, "y must be >= 0", Square, 2, 4, -7)

    def test_string_width(self):
        self.assertRaisesRegex(TypeError, "width must be an integer", Square, "3", 6)

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
        self.assertEqual(squa.id, 43)

    def test_update_one_argument(self):
        squa = Square(1,1)
        squa.update(5)
        self.assertEqual(squa.id, 5)

    def test_to_dictionary(self):
        squa = Square(10, 2, 3, 1)
        expected_dict = {
            'id': 1,
            'width': 10,
            'x': 2,
            'y': 3
        }
        self.assertEqual(squa.to_dictionary(), expected_dict)

    def test_square_save_none(self):
        try:
            Base.save_to_file(None)
            with open("Square.json", "r") as f:
                self.assertEqual(f.read(), "[]")
        except:
            self.assertRaises(FileNotFoundError)

    def test_square_save_empty_list(self):
        try:
            Base.save_to_file([])
            with open("Square.json", "r") as f:
                self.assertEqual(f.read(), "[]")
        except:
            self.assertRaises(FileNotFoundError)

    def test_square_save_valid_objects(self):
        try:
            s1 = Square(3, id=42)
            s2 = Square(5)
            Square.save_to_file([s1, s2])
            
            expected_json = (
                '[{"id": 42, "size": 3, "x": 0, "y": 0}, '
                '{"id": 1, "sizw": 5, "x": 0, "y": 0}]'
            )
            with open("Square.json", "r") as f:
                self.assertEqual(f.read(), expected_json)
        except:
            self.assertRaises(FileNotFoundError)

    def test_create_square(self):
        sqaure = Square(1)
        new_square = sqaure.create(**{ 'id': 89, 'size': 5, 'x': 3, 'y': 2 })
        self.assertEqual(new_square.id, 89)
        self.assertEqual(new_square.size, 5)
        self.assertEqual(new_square.x, 3)
        self.assertEqual(new_square.y, 2)


    def test_save_empty_list(self):
        """Test saving an empty list"""
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

    def test_save_none(self):
        """Test saving None"""
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

    def test_save_one_square(self):
        """Test saving one rectangle"""
        s = Square(10, 2, 8, 1)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))
        
        expected = '[{"id": 1, "width": 10, "x": 2, "y": 8}]'
        with open("Square.json", 'r') as f:
            self.assertEqual(f.read(), expected)

    def test_save_two_squares(self):
        """Test saving two rectangles"""
        s1 = Square(10, 2, 8, 1)
        s2 = Square(2, 0, 0, 2)
        Square.save_to_file([s1, s2])
        self.assertTrue(os.path.exists("Square.json"))
        
        expected = (
            '[{"id": 1, "width": 10, "x": 2, "y": 8}, '
            '{"id": 2, "width": 2, "x": 0, "y": 0}]'
        )
        with open("Square.json", 'r') as f:
            self.assertEqual(f.read(), expected)

    def test_save_file_overwrite(self):
        """Test that existing file is overwritten"""
        # First save
        s1 = Square(1, 0, 0, 1)
        Square.save_to_file([s1])
        
        # Second save with different data
        s2 = Square(2, 0, 0, 2)
        Square.save_to_file([s2])
        
        expected = '[{"id": 2, "width": 2, "x": 0, "y": 0}]'
        with open("Square.json", 'r') as f:
            self.assertEqual(f.read(), expected)

    def test_save_invalid_object(self):
        """Test saving invalid objects (should raise AttributeError)"""
        with self.assertRaises(AttributeError):
            Square.save_to_file([1, 2, 3])

    def test_filename_correct(self):
        """Test that filename is correct"""
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))