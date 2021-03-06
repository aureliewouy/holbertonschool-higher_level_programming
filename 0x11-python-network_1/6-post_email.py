#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter"""
import requests
import sys


if __name__ == "__main__":
    """code should not be executed when imported"""
    email = {'email': sys.argv[2]}
    url = sys.argv[1]
    r = requests.post(url, data=email)
    print(r.text)
