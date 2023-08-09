#!/usr/bin/python3
for code in range(97, 123):
    if chr(code) in "qe":
        continue
    print("{}".format(chr(code)), end="")
