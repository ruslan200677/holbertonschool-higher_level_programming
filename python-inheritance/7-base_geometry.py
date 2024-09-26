#!/usr/bin/python3
"""python3"""


class BaseGeometry:
    """ class base"""
    def area(self):
        raise Exception("area() is not implemented")
    

def integer_validator(self, name, value):
    """valildator"""

    if not isinstance(value, int):
        raise TypeError("<name> must be an integer")
    if value <= 0:
        raise ValueError("<name> must be greater than 0")