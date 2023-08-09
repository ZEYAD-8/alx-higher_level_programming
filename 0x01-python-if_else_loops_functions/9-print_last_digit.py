#!/usr/bin/python3
def print_last_digit(number):
    if type(number) != int:
        raise TypeError
    last_digit = str(number)[-1]
    print("{}".format(last_digit), end="")
    return last_digit
