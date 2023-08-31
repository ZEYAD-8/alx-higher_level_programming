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
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if ((type(value) != tuple) or (len(value)) != 2 or
                (type(value[0]) != int) or (value[0] < 0) or
                (type(value[1]) != int) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        pos1 = self.__position[0]
        pos2 = self.__position[1]

        if self.__size == 0:
            print("")
        for i in range(pos2):
            print("")
        for s in range(self.__size):
            for r in range(pos1):
                print(" ", end='')
            for c in range(self.__size):
                print("#", end="")
            print("")
