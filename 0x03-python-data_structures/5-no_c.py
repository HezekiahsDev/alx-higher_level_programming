#!/usr/bin/python3
def no_c(my_string):
    edit = my_string[:]
    size = len(my_string)
    i = 0

    for char in range(size):
        if my_string[char] == 'C' or my_string[char] == 'c':
            edit = edit[:(char - i):] + my_string[(char + 1):]
            i = i + 1
        return edit
