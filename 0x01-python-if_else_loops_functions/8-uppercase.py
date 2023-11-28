#!/usr/bin/python3
# this function print a string in uppercase

def uppercase(str):

    for char in str:
        if 'a' <= char <= 'z':
            upperCHAR = chr(ord(char) - 32)
        else:
            upperCHAR = char
            print('{}'.format(upperCHAR), end='\n')
