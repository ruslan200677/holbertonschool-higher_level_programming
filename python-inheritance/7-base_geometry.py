#!/usr/bin/python3
"""python3"""


class BaseGeometry:
    """ class base"""
    def area(self):
        """salam"""
        raise Exception("area() is not implemented")
    

def integer_validator(self, name, value):
    """valildator"""

    if not isinstance(value, int):
        raise TypeError('{} must be an integer'.format(name))
    if value <= 0:
        raise ValueError('{} must be greater than 0'.format(name))