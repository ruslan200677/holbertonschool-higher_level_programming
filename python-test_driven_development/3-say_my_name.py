#!/usr/bin/python3
""" Module contains function say my name """
def greet_person(first_name, last_name):
    """Function to greet a person by their first and last names"""
    
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    return f"Hello, {first_name} {last_name}!"
