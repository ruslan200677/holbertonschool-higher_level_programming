#!/usr/bin/python3
"""module"""


import json


def save_to_json_file(my_obj, filename):
    """func00"""

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
