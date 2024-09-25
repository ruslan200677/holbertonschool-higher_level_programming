#!/usr/bin/python3
''' usr bin'''

def is_same_class(obj, a_class):
    '''Return True if obj is exactly an instance of a_class; otherwise False.'''
    if type(obj) is a_class:
        return True
    return False