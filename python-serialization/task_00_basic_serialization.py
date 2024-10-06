#!/usr/bin/python3
"""Module containing basic serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """Function to serialize and save to the specified file"""

    
    content = json.dumps(data)
    with open(filename, 'w') as file:
        file.write(content)


def load_and_deserialize(filename):
    """Function to load and deserialize"""

    
    with open(filename, 'r', encoding='UTF-8') as file:
        content = file.read()

    return json.loads(content)
