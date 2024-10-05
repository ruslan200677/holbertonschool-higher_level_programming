#!/usr/bin/python3
""" json"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """ class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dict"""
        return self.__dict__