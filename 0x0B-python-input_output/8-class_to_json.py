#!/usr/bin/python3
"""
8. Class to JSON
"""
import json


def class_to_json(obj):
    """
    a function that returns the dictionary description
    """
    return json.dumps(obj.__dict__)
