#!/usr/bin/oython3
import random
number = random.randit(-10000,10000)
a = number % 10
if number < 0:
    a = (number % 10) - 10
if a > 5:
    print(f"Last digit of {number} is {a} and is greater than 5")
elif a == 0:
    print(f"Last digit of {number} is {a} amd is 0")
else:
    print(f"Last digit of {number} is {a} and is less than 6 and not 0")
