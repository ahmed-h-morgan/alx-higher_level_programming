#!/usr/bin/python3
"""unittest using u-test python module"""

import unittest
max_integer_module = __import__('6-max_integer')
class TestMaxInteger(unittest.TestCase):
    """unit tests class"""

    def test_int(self):
        self.assertEqual(max_integer_module.max_integer([10, 7, 3]), 10)
        self.assertEqual(max_integer_module.max_integer([1, 4, 2]), 4)
        self.assertEqual(max_integer_module.max_integer([3, 5, 15]), 15)
        self.assertEqual(max_integer_module.max_integer([-10, 7, 3]), 7)
        self.assertEqual(max_integer_module.max_integer([-10, -7, -3]), -3)

    def test_one_element(self):
        self.assertEqual(max_integer_module.max_integer([10]), 10)

    def test_empty_list(self):
        self.assertEqual(max_integer_module.max_integer([]), None)
    
    def test_char(self):
        # self.assertRaises(TypeError, max_integer_module.max_integer, [1, 2, 'k', 4])
        with self.assertRaises(TypeError):
            max_integer_module.max_integer([1, 2, 'k', 4])


if __name__ == '__main__':
    unittest.main()