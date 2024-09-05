#!/usr/bin/python3
import random

number = random.randint(-10000, 10000) % 10
a = number % 10

if a > 5:
    print(f"{a} is greater than 5")
elif a == 0:
    print(f"{a} is 0")
else:
    print(f"{a} is less than 6 and not 0")
