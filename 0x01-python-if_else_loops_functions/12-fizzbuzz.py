#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        Done = False
        if num % 3 == 0:
            print("Fizz", end="")
            Done = True
        if num % 5 == 0:
            print("Buzz", end="")
            Done = True
        if not Done:
            print(num, end="")
        print(" ", end="")
