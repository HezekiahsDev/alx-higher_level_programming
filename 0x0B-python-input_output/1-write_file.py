#!/usr/bin/python3
"""This script defines a function that writes into a UTF-8 file"""


def write_file(filename="", text=""):
    """Writw into file
    """
    with open(filename, "w", encoding="utf-8") as f:
        write_text = f.write(text)
        return write_text
