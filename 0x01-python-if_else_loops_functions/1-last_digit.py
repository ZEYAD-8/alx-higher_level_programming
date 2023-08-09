#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if type(number) != int:
    number[-1]
num = str(number)
last_digit = int(num[-1])
if number < 0:
    last_digit *= -1

print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 but not 0")
