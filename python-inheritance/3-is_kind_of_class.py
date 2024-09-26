#!/usr/bin/python3
""" function"""


def is_kind_of_class(obj, a_class):
    """ func returns inherit"""

    if isinstance(obj, a_class):
        return True
    else:
        return False