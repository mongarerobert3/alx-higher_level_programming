#!/usr/bin/python3
"""function that writes an Object to a text file,
using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """logic
            Args:
                my_obj - object to write to
                filename - name of file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
