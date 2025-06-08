#!/usr/bin/python3
"""
    Prototype: def read_file(filename=""):
    You must use the with statement
    You don’t need to manage file permission or file doesn't exist exceptions.
    You are not allowed to import any module
"""


def read_file(filename=""):
    """raed a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
