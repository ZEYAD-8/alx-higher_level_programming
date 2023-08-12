#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)

    sum = 0
    for num in range(1, length):
        sum += int(argv[num])
    print(sum)
