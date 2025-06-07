#!/usr/bin/python3
"""BaseGeometry - module"""


class BaseGeometry:
    """new base geometry class"""
    # def __init__(self, name, value):
    #     self.name = name
    #     self.value = value

    def area(self):
        """rais exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """value validator"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
