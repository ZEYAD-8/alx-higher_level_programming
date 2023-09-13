#!/usr/bin/python3
"""module to read a text file with UTF8 and prints to stdout"""


def read_file(filename=""):
    """function to read the file"""
    with open(filename, encoding="UTF8") as file:
        print(file.read())
