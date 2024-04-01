#!/usr/bin/python3
"""This script contains a function that add
    unique elements together
"""

def uniq_add(my_list=[]):
    n = 0
    for elem in set(my_list):
        n += elem
    return n
