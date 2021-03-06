#!/usr/bin/python3
"""
    Definition for a LockedClass class.
    """


class LockedClass():
    """A locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
