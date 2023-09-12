#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Defines a rectangle class.
"""


class Rectangle(BaseGeometry):
    """a Rectangle class that inherits from basegeometry class"""
    def __init__(self, width, height):
        """initialize"""
        BaseGeometry.integer_validator(BaseGeometry, "width", width)
        Rectangle.integer_validator(Rectangle, "height", height)
        self.__width = width
        self.__height = height
