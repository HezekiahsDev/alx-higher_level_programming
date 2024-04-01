#!/usr/bin/python3
"""This script search and replace an element
    in an array
"""

def search_replace(my_list, search, replace):
    def find_elem(elem):
        if elem == search:
            return replace
        else:
            return elem
    res = list(map(find_elem, my_list))
    return res
