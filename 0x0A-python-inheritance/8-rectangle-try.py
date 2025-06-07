#!/usr/bin/python3
"""rectangle mod"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle from base"""
    def __init__(self, width, height):
        """init func"""

        if self.integer_validator("height", height) or\
                self.integer_validator("width", width):

            self._width = width
            self.height = height
