#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
print(f"Last digit of {number} is {num[-1]}", end=" ")
if int(num[-1]) > 5:
    print("and is greater than 5")
elif int(num[-1]) == 0:
    print("and is 0")
else:
    print("and is less than 6 but not 0")