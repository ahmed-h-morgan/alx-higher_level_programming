#!/usr/bin/python3
"""
0. Read file
"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8)
    """
    with open(filename, 'r', encoding="UTF8") as file:
        for line in file:
            print(line, end='')
