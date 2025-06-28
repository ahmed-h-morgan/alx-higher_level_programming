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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): a list of instances who inherits of Base
        """
        if not list_objs:
            with open(f"{cls.__name__}.json", 'w') as file:
                file.write("[]")
        else:
            dict_list = []
            for object in list_objs:
                dict_list.append(object.to_dictionary())
            
            with open(f"{cls.__name__}.json", 'w') as file:
                file.write(cls.to_json_string(dict_list))
                