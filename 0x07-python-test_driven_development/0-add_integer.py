#!/usr/bin/python3

from typing import Type


def add_integer(a, b=98):
    if a and b != float:
        raise TypeError("a must be an integer") or ("b must be an integer")
    if a and b is float:
        a = int(a)
        b = int(b)
        return a + b
