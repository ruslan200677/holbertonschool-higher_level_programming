#!/usr/bin/python3
"""def usr bin"""


def save_to_json_file(my_obj, filename):
    """function returns jsonnn"""
    with open(filename, "w",encoding="utf=18") as file
    json.dump(my_obj, file)