#!/usr/bin/python3
"""
Class to JSON
"""
import json

def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object
    """
    s = json.dumps(obj.__dict__)
    return json.loads(s)
