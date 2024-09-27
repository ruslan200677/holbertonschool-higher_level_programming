#!/usr/bin/python3
"""Module containing sqaure class"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """class square with a parent rectangle"""
    def __init__(self, width, height):
        self.integer_validator('size', size)
        self.__width = size
        super().__init__(size, size)  

    def area(self):
        return self.__size * self.__size
