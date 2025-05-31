#!/usr/bin/python3
"""Module for lazy matrix multiplication using NumPy"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy with proper error handling
    
    Args:
        m_a: First matrix (list of lists)
        m_b: Second matrix (list of lists)
    
    Returns:
        Resulting matrix product as a NumPy array
    
    Raises:
        TypeError: For invalid input types
        ValueError: For empty matrices or incompatible dimensions
    """
    # Input type validation
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    # Check if inputs are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    # Check for empty matrices
    if len(m_a) == 0 or (len(m_a) > 0 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) > 0 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    
    # Validate matrix contents
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    
    # Check multiplication compatibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Perform matrix multiplication using NumPy
    return np.matmul(m_a, m_b)