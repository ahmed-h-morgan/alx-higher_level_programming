#!/usr/bin/python3
class Square:
   """
   This class defines a square by its size.
   """
   def __init__(self, size):
       """
       The constructor for the Square class.

       Args:
           size (int): The size of the square.
       """
       self.__size = size

   def get_size(self):
       """
       This method returns the size of the square.

       Returns:
           int: The size of the square.
       """
       return self.__size
