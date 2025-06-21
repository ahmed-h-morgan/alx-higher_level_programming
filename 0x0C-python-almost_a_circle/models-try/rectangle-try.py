#!/usr/bin/python3
"""the rectangle module"""
from models.base import Base


class Rectangle(Base):
    """the rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """rectanglr attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """claculating the instance area"""
        return self.__width * self.__height

    def display(self):
        """display symbole"""
        for vertical in range(self.__y):
            print()
        for symbole in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self) -> str:
        return f"[Rectangle] " + \
            f"({self.id}) {self.__x}/{self.__y} " + \
            f"- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """specify the arguments"""
        if len(args) > 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.__width = args[1]
            if len(args) == 3:
                self.__height = args[2]
            if len(args) == 4:
                self.__x = args[3]
            if len(args) == 5:
                self.__y = args[4]

        if args:
            return

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """

        rect_dict = {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
        return rect_dict
