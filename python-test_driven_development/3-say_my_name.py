#!/usr/bin/python3
""" Module contains function say my name """
def say_my_name(first_name, last_name=""):
    """ salammm """

    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string and last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))