#!/usr/bin/python3

# this function remove character at a given index

def remove_char_at(str, n):
    if n >= 0:
        r = str[0:n] + str[n + 1:]
        return r
    return str
