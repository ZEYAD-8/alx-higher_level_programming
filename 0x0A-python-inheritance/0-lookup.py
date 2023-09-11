#!/usr/bin/python3
"""A module to define lookup function"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return dir(obj)
