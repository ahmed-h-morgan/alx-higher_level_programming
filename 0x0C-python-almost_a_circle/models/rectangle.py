#!/usr/bin/python3
"""
2. First Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    create the rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """
        calculate rectangle area
        Returns:
            int: total area of rectangle
        """
        return self.width * self.height

    # def display(self):
    #     """
    #     draw rectangle shape on terminal
    #     """
    #     for h in range(self.height):
    #         row = ""
    #         for w in range(self.width):
    #             row += "#"
    #         print(row)

    def __str__(self):
        return f"[Rectangle] " + \
            f"({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def display(self):
        """display symbole"""
        for vertical in range(self.y):
            print()
        for symbole in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args):
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]  
            self.width = args[1]
        elif len(args) == 3:
            self.id = args[0]  
            self.width = args[1]
            self.height = args[2]
        elif len(args) == 4:
            self.id = args[0]  
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
        elif len(args) == 5:
            self.id = args[0]  
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

