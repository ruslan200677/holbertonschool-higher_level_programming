#!/usr/bin/python3
from add_0 import add

def main():
    a = 1
    b = 2
    result = add(a, b)
    # Use .format() method to format the output
    print("{} + {} = {}".format(a, b, result))

if __name__ == "__main__":
    main()

