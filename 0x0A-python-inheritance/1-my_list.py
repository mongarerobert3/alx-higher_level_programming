#!/usr/bin/python3
""""class MyList that inherits from list"""


class MyList(list):
    """Instance Method"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
