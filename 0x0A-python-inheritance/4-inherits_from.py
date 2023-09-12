#!/usr/bin/python3
"""
Defines a class and inherited class-checking function.
"""


def inherits_from(obj, a_class):
    """Check if an object is an instance or inherited instance of a class."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
