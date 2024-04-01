#!/usr/bin/python3
"""This script contains a function that returns
    a set of all elements present in only one set
"""


def only_diff_elements(set_1, set_2):
    res = (set_1 ^ set_2)
    return res
