#!/usr/bin/python3
"""
contains the JSON str to an function
"""

import JSON


def from_json_string(my_str):
    """
    returns an object represented by a JSON string
    """
    return json.loads(my_str)
