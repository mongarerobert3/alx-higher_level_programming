#!/usr/bin/python3
"""function that returns an object (Python data structure)
represented by a JSON string:"""


import json


def from_json_string(my_str):
    """Args:
            loads - function to read json file
            my_str - to read from
    """
    return json.loads(my_str)
