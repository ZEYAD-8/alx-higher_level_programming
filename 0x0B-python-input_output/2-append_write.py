#!/usr/bin/python3
"""module to open a file and write text"""


def append_write(filename="", text=""):
    """function to read the file"""
    if filename == "" or text == "":
        return
    with open(filename, mode="a", encoding="UTF8") as file:
        return file.write(text)
