#!/usr/bin/python3
"""SALAM"""


def add_integer(a, b=98):
    """SALAM2"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a+b)
