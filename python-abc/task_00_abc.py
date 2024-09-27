#!/usr/bin/python3
from abc import ABC

class Animal(ABC):
    """ class animal"""


class Dog(Animal):
    """s"""
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    """dwedwd"""
    def sound(self):
        return "Meow"