#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    """code should not be executed when imported"""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        body = response.headers
        id = body.get('X-Request-Id')
        print(id)
