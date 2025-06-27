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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """

        squar_dict = {
            'id': self.id,
            'width': self.width,
            'x': self.x,
            'y': self.y
        }
        return squar_dict
