#!/usr/bin/python3
class Square:
  """
  This class defines a square by its size and position.
  """
  def __init__(self, size=0, position=(0, 0)):
      """
      The constructor for the Square class.

      Args:
          size (int): The size of the square.
          position (tuple): The position of the square.
      """
      self.size = size
      self.position = position

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

  @property
  def position(self):
      """
      This method returns the position of the square.

      Returns:
          tuple: The position of the square.
      """
      return self.__position

  @position.setter
  def position(self, value):
      """
      This method sets the position of the square.

      Args:
          value (tuple): The new position of the square.
      """
      if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int) and x >= 0 for x in value):
          raise TypeError("position must be a tuple of 2 positive integers")
      self.__position = value

  def area(self):
      """
      This method returns the area of the square.

      Returns:
          int: The area of the square.
      """
      return self.__size ** 2

  def my_print(self):
      """
      This method prints the square with the character #.
      """
      for i in range(self.__position[1]):
          print()
      for i in range(self.__size):
          print(" " * self.__position[0] + "#" * self.__size)
