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
       self.size = size

   @property
   def size(self):
       """
       This method returns the size of the square.

       Returns:
           int: The size of the square.
       """
       return self.__size

   @size.setter
   def size(self, value):
       """
       This method sets the size of the square.

       Args:
           value (int): The new size of the square.
       """
       if not isinstance(value, int):
           raise TypeError("size must be an integer")
       if value < 0:
           raise ValueError("size must be >= 0")
       self.__size = value

   def area(self):
       """
       This method returns the area of the square.

       Returns:
           int: The area of the square.
       """
       return self.__size ** 2
