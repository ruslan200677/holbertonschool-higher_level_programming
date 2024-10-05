#!/usr/bin/python3
"""function"""
import json


def save_to_json_file(my_obj, filename):
    """JSON """
    with open(filename, "w") as file:
        json.dump(my_obj, f)