#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    """code should not be executed when imported"""
    url = sys.argv[1]
    response = requests.get(url)
    h = response.headers
    id = h.get('X-Request-Id')
    print(id)
