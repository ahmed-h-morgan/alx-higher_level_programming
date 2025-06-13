#!/usr/bin/python3
"""
9. Student to JSON
"""


class Student:
    """
    class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        """
        class Student that defines a student by: (based on 9-student.py)
        """
        result_dic = {}

        if attrs is None:
            return self.__dict__

        if len(attrs) == 0:
            return {}

        if not isinstance(attrs, list) or not\
           all(isinstance(attr, str) for attr in attrs):
            return self.__dict__
        # for attribute in attrs:
        #     if not isinstance(attribute, str):
        #         return self.__dict__

        for attribute in attrs:
            for keys, values in self.__dict__.items():
                if attribute in keys:
                    result_dic[attribute] = values
        return result_dic

    def reload_from_json(self, json):
        if len(json) == 0:
            pass
        for key_att in json:
            if key_att in self.__dict__:
                self.__dict__[key_att] = json[key_att]
