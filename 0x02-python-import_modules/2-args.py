#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)

    print(length - 1, end=" ")
    if length == 1:
        print("arguments.")
    elif length == 2:
        print("argument:")
    elif length > 2:
        print("arguments:")

    counter = 1
    for _ in range(0, length - counter):
        print("{}: {}".format(counter, argv[counter]))
        counter += 1
