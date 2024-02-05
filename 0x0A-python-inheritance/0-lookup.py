#!/usr/bin/python3
"""
    This script provides module which has a function that retrieves the list of attributes
    and methods associated with a given object.
"""


def lookup(obj):
    """This function identifies all attributes and methods associated with an object."""
    return dir(obj)

