#!/usr/bin/python3
"""
Defines a class and inherited class-checking function.
"""


class BaseGeometry:
    """Base class contains area function"""
    def area(self):
        """ raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
