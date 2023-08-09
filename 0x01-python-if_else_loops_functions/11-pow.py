#!/usr/bin/python3
def pow(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError
    if b == 0:
        return 1
    elif b > 0:
        result = 1
        for _ in range(b):
            result *= a
        return result
    else:
        reciprocal_result = 1
        for _ in range(-b):
            reciprocal_result *= a
        return 1 / reciprocal_result
