#!/usr/bin/python3
"""
12. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # Every row starts with 1

        # Calculate the middle elements
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])

        new_row.append(1)  # Every row ends with 1
        triangle.append(new_row)

    return triangle
