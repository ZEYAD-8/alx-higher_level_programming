#!/usr/bin/python3
def pow(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError
    return a ^ b
