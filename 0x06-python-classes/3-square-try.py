#!/usr/bin/python3
"""Square the number. """


class Square:
    """Define a square class. """

    def __init__(self, size=0):
        """
        Parameters
        ----------
            size : the size of the square.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculating the current square area"""
        return self.__size ** 2
