#!/usr/bin/python3
"""salam"""


def append_write(filename="", text=""):
    """ salmammm"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
