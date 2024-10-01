#!/usr/bin/python3
"""Module usr"""


def read_file(filename=""):
    """function read"""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")