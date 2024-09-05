#!/usr/bin/python3
import random

number = random.randint(-10000, 10000) 
last digit  = number % 10
if number < 0:
    last digit = (number % 10) - 10
if last digit > 5:
    print(f" Last digit of {number} is {last digit} and is greater than 5")
elif last digit == 0:
    print(f"Last digit of {number} is {last digit} and is 0")
else:
    print(f"Last digit of {number} is {last digit} and is less than 6 and not 0")
