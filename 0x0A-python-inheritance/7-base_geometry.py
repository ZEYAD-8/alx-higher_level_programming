#!/usr/bin/python3
"""
Defines a class and inherited class-checking function.
"""


class BaseGeometry:
    """Base Geometry class object"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is int or larger than 0"""

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
