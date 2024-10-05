#!/usr/bin/python3
"""function"""



def save_to_json_file(my_obj, filename):
    """JSON """
    import json
    with open(filename, "w") as file:
        json.dump(my_obj, f)