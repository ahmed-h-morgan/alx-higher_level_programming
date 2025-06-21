#!/usr/bin/python3
""" the base class"""
import json


class Base:
    """the base of all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """manage id attribute in all your future classes\
            and to avoid duplicating the same code
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """"returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        str_rep = json.dumps(list_dictionaries)
        return str_rep

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        if list_objs is None:
            list_objs = []

        class_name = cls.__name__

        file_name = f"{class_name}.json"
        json_string = cls.to_json_string(list_objs)

        with open(file_name, 'w') as file:
            file.write(json_string)
