#!/usr/bin/python3
"""
1. My list
"""


class MyList (list):
    """
    customized list
    """

    def print_sorted(self):
        """
        print sorted list
        """
        print(sorted(self))
