#!/usr/bin/python3
"""This script defines a function that apends a UTF-8 file"""


def append_write(filename="", text=""):
    """Append file
    """
    with open(filename, "a", encoding="utf-8") as f:
        append_text = f.write(text)
        return append_text
