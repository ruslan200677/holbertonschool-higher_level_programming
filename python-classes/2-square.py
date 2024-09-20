#!/usr/bin/python3
"""Module for creating empty class"""


class Square():
    """Define class"""
    def __init__(self, size):
        """Initialize the square with a given size."""
        if not isinstance(size, int):
            raise TypeError ("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    pass
