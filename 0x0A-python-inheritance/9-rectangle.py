#!/usr/bin/python3
"""
Defines a rectangle class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from basegeometry class"""
    def __init__(self, width, height):
        """initialize a new Rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return The area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return "[Rectangle] " + str(self.width) + "/" + str(self.height)
