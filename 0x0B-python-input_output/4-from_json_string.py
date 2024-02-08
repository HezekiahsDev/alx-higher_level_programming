#!/bin/python3
import json

def from_json_string(my_str):
    """
    Convert a JSON string into a Python object

    Args:
    my_str (str): A JSON string representing a Python object.

    Returns:
    object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
