#!/usr/bin/python3
"""
0. Read file
"""


def read_file(filename=""):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
