#!/usr/bin/python3
newline = False
for tens in range(10):
    for ones in range(10):
        if tens == 8 and ones == 9:
            newline = True
        if tens < ones:
            print("{}{}".format(tens, ones), end=", " if not newline else "\n")
