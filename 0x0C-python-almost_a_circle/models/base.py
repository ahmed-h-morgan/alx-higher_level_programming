#!/usr/bin/python3
"""
1. Base class
"""
import json


class Base:
    """
    create the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """"returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        str_rep = json.dumps(list_dictionaries)
        return str_rep
