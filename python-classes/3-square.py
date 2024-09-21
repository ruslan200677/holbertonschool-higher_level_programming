#!/usr/bin/python3
"""Module for creating a class that defines a square."""


class Square:
    """Class that defines a square with a given size."""
    
    def __init__(self, size=0):
        """Initialize the square with a given size."""

        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size