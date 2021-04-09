#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response"""
import requests
import sys
from requests.exceptions import HTTPError


if __name__ == "__main__":
    """code should not be executed when imported"""
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except HTTPError as http_err:
        print('Error code: {}'.format(response.status_code))
