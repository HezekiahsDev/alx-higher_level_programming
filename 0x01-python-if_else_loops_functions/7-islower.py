#!/usr/bin/python3

# slower - checks is a character is lowercase
# Return: true or false

def islower(c):

    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
