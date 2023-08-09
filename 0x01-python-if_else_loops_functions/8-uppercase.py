#!/usr/bin/python3
def uppercase(str):
    for character in range(len(str)):
        if ord(character) in range (97, 123):
            character = ord(character) - 32
        print("{}".format(character), end="")
    print()
