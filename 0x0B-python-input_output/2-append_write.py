#!/usr/bin/python3
"""function that writes a string to a text file (UTF8) 
and returns the number of characters written:"""


def write_file(filename="", text=""):
    """writing the string
        Args:
            filename (str): The name of the file to write to
            text (str): text to write
        Return:
            The number of chars
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
