#!/usr/bin/python3
"""
5. Save Object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    with open(filename, 'w') as file:
        js_string = json.dumps(my_obj)
        return file.write(js_string)
