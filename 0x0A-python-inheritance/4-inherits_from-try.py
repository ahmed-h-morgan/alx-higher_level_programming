#!/usr/bin/python3
"""check subclass"""


def inherits_from(obj, a_class):
    """check subclass"""
    if (type(obj) is a_class):
        return False
    elif isinstance(obj, a_class):
        return True
    # elif type(obj) is a_class:
    #     return False
