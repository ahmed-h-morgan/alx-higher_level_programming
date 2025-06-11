#!/usr/bin/python3
"""
6. Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    with open(filename, 'r+') as file:
        return json.load(file)
