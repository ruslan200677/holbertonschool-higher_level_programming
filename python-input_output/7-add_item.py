#!/usr/bin/python3
"""function"""
import json


def save_to_json_file(my_obj, filename):
    """JSON """
    with open(filename, "w") as f:
        json.dump(my_obj, f)