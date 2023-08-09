#!/usr/bin/python3
def pow(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError
    res = 0
    for iteration in range(b):
        res = res + (a * a)
    return res
