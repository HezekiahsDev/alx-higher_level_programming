#!/usr/bin/python3

# this function print the last digit of a number

def print_last_digit(number):

    # check if number is a valid int
    if not isinstance(number, int):
        print("Error: Please provide an integer")
        return None

    # get last digit
    return (abs(number) % 10)
