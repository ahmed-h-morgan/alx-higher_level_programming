#!/usr/bin/python3
"""the inhereted square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the square chape class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing thw square"""
        super().__init__(size, size, x, y, id)
        # self.size = size

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

    def __str__(self):
        """overriding the __str__ method of the reqtangle parent class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """specify the arguments"""
        if len(args) > 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]

        if args:
            return

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        square_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
        return square_dict
