#!/usr/bin/python3
"""This script defines a function that converts a string to JSON"""
import json


def to_json_string(my_obj):
    """Return JSON format"""
    ret = json.dumps(my_obj)
    return ret
