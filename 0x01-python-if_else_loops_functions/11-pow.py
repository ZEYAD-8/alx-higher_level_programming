#!/usr/bin/python3
def pow(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError
    res = 1
    for _ in range(b):
        res *= a
    return res
