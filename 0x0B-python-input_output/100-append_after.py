#!/usr/bin/python3
"""
    13. Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, 'r+') as file:
        content = file.read()
        file.write(content.replace(search_string, new_string))
