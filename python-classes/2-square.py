#!/usr/bin/python3
"""Module for creating a class that defines a square."""


class Square:
    """Class that defines a square with a given size."""
    
    def __init__(self, size):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square's side.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size