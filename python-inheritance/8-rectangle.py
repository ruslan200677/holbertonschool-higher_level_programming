#!/usr/bin/python3
"""salam"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """iiy8y87"""
        self.__width = width  
        self.__height = height  
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)  