#!/usr/bin/python3
def no_c(my_string):
    edit = ""

    for char in my_string:
        if char != 'C' and char != 'c':
            edit = edit + char
        return edit
