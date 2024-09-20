#!/usr/bin/python3
"""Module for creating empty class"""


class Square():
    """Define class"""
    def __init__(self, size):
        if isinstance(size, int):
            raise TypeError ("salamm")
        if size < 0:
            raise ValueError("salma")
        self.__size = size
    pass
