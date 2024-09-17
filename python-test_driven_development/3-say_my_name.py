#!/usr/bin/python3
"""Module contains function say_my_name"""


def say_my_name(first_name, last_name=""):
    """
    Print the full name by combining the first name and optional last name.

    Args:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed. Default is "".

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
