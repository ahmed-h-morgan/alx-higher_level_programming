#!/usr/bin/python3
"""
    The square size
"""


class Square:
    """
        Building Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("size must be a tuple")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not map(lambda x: True if (x > 0) else False, position):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not map(lambda x: True if (isinstance(x, int)) else False,
                     position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("size must be a tuple")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not map(lambda x: True if (x > 0) else False, value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not map(lambda x: True if (isinstance(x, int)) else False, value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        # if self.__size == 0:
        #     print()
        # else:

        #     for x in range(self.__size):
        #         text = ""
        #         for y in range(self.__size):
        #             text += '#'
        #         print(text)
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
