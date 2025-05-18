#!/usr/bin/python3
import math
"""
    Define a MagicClass that mimics the given bytecode behavior
"""


class MagicClass:
    """
    A circle-like class with radius-based geometry calculations.

    This class provides methods to calculate the area and circumference
    of a circle based on its radius, following the exact behavior
    shown in the provided bytecode disassembly.

    Attributes:
        __radius (int/float): The radius of the circle (private).
    """
    
    def __init__(self, radius=0):
        """
        Initialize MagicClass with a radius.
        
        Args:
            radius (int/float): Radius of the circle (default 0)
        
        Raises:
            TypeError: If radius is not a number
        """
        self.__radius = 0  # Initialize to 0 first (line 10 in bytecode)
        
        # Type checking (lines 11-12 in bytecode)
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        
        self.__radius = radius  # Store the radius (line 13 in bytecode)

    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (πr²)
        """
        return (self.__radius ** 2) * math.pi  # (lines 17-20 in bytecode)

    def circumference(self):
        """
        Calculate the circumference of the circle.
        
        Returns:
            float: The circumference of the circle (2πr)
        """
        return 2 * math.pi * self.__radius  # (lines 21-24 in bytecode)
