#!/usr/bin/python3
def add(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError
    return a + b
