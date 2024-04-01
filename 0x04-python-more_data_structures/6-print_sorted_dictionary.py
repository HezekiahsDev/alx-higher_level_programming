#!/usr/bin/python3
"""Tjis script contains a funtion that ptints
    a sorted form of a dictionary
"""


def print_sorted_dictionary(a_dictionary):
    i = sorted(a_dictionary.keys())
    for keys in i:
        print('{}: {}'.format(keys, a_dictionary[keys]))
