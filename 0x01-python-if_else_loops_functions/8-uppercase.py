#!/usr/bin/python3
# this function print a string in uppercase

def uppercase(str):

    disp_str = ''

    for char in str:
        if 'a' <= char <= 'z':
            disp_str += chr(ord(char) - 32)
        else:
            disp_str += char
    print("{disp_str}", end="")
