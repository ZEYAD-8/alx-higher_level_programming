#!/usr/bin/python3
"""Square with size"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        """Property setter to set position"""
        if ((type(value) != tuple) or (len(value) != 2) or
                (type(value[0]) != int) or (value[0] < 0) or
                (type(value[1]) != int) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for lin in range(self.__position[1]):
            print("")
        for r in range(self.__size):
            for s in range(self.__position[0]):
                print(" ", end="")
            for c in range(self.__size):
                print("#", end="")
            print("")

    def __str__(self):
        for line in range(self.__position[1]):
            print("")
        for r in range(self.__size):
            for s in range(self.__position[0]):
                print(" ", end="")
            for c in range(self.__size):
                print("#", end="")
            if (r != self.__size - 1):
                print("")
        return ("")
