#!/usr/bin/python3

# this function print the last digit of a number

def print_last_digit(number):

    r = (abs(number) % 10)
    print(r, end='')
    return r
