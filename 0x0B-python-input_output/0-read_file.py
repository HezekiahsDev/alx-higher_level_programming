#!/usr/bin/python3
"""This script defines a function that opens and prints a UTF-8 file"""


def read_file(filename=""):
    """print file content"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
