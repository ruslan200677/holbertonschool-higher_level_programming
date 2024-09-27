#!/usr/bin/python3
"""Module containing BaseGeometry class"""
Rectangle = __import__(9-rectangle.py).Rectangle



class Square(Rectangle):
    """class rectangle with a parent basegeometry"""
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        return self.__width * self.__height
