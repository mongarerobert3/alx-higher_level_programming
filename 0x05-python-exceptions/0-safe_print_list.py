#!/usr/bin/python3

from msilib.schema import Error


def safe_print_list(my_list=[], x=0):
    try:
        print("{}".format(my_list))
    except Error:
        print("List is empty")
