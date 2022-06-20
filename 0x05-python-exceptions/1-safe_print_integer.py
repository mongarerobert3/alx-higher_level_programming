#!/usr/bin/python3

def safe_print_integer(value):
    if value is int:
        try:
            print("{:d}".format())
        except ValueError:
            return 1
