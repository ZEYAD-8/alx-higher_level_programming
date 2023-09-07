#!/usr/bin/python3
"""rectangle class module"""


class Rectangle:
    """rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        print_hash_str = str(self.print_symbol)
        rectangle_str = ''
        for i in range(self.__height):
            rectangle_str += print_hash_str * self.__width
            if i == self.__height - 1:
                break
            rectangle_str += "\n"
        return (rectangle_str)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__heighth})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_one = rect_1.area()
        area_two = rect_2.area()

        if area_one > area_two:
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
