#!/usr/bin/python3
"""reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """opening the file"""
    with open(filename, encoding="utf_8") as f:
        read_data = f.read()
        print(read_data)
