#!/usr/bin/python3
class Square:
 """
 This class defines a square by its size.
 """
 def __init__(self, size=0):
     """
     The constructor for the Square class.

     Args:
         size (int): The size of the square.
     """
     if not isinstance(size, int):
         raise TypeError("size must be an integer")
     if size < 0:
         raise ValueError("size must be >= 0")
     self.__size = size

 def get_size(self):
     """
     This method returns the size of the square.

     Returns:
         int: The size of the square.
     """
     return self.__size

 def area(self):
     """
     This method returns the area of the square.

     Returns:
         int: The area of the square.
     """
     return self.__size ** 2
