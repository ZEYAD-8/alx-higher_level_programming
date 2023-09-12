#!/usr/bin/python3
"""
    module that contains the definition of MyList Class
"""


class MyList(list):
    """prints the list but sorted (ascending sort)"""
    def print_sorted(self):
        print(sorted(self))
