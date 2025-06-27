#!/usr/bin/python3
"""
10. First Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class to create Square shape
    based on Rectangle class

    Args:
        Rectangle (Class): the parent of the Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
