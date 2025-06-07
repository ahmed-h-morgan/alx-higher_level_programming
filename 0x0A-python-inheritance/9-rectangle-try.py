#!/usr/bin/python3
"""printing rectangle area"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle from base"""
    def __init__(self, width, height):
        """init func"""
        super().__init__()
        if self.integer_validator("height", height) or\
                self.integer_validator("width", width):

            self._width = width
            self.height = height
    @classmethod
    def area(self):
        # super().area()
        try:
            print(f"[Rectangle] {self._width}/{self.height}")
            return self._width / self.height
        except:
            super().area()
