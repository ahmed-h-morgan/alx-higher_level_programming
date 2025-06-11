#!/usr/bin/python3
"""
6. Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a "JSON file"
    """
    with open(filename, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                "Expecting property name enclosed in double quotes",
                e.doc, e.pos) from None
