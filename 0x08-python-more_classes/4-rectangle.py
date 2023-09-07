#!/usr/bin/python3
"""rectangle class module"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return (self.__width * self.height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2*self.__width)+(2*self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        rectangle_str = ''
        for i in range(self.__height):
            rectangle_str += "#" * self.__width
            if i == self.__height - 1:
                break
            rectangle_str += "\n"
        return (rectangle_str)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
