#!/usr/bin/python3
"""usr bin"""


def write_file(filename="", text=""):
    """function returbs a text"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)