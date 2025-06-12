#!/usr/bin/python3
"""
8. Class to JSON
"""


def class_to_json(obj):
    """
    a function that returns the dictionary description
    """
    return obj.__dict__
