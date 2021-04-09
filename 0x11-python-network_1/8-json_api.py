#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request """
import requests
import sys


if __name__ == "__main__":
    """code should not be executed when imported"""
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        letter = {'q': ""}
    else:
        letter = {'q': sys.argv[1]}
    r = requests.post(url, data=letter)
    try:
        jsn = r.json()
        if not jsn:
            print("No result")
        else:
            print("[{}] {}".format(jsn['id'], jsn['name']))
    except:
        print("Not a valid JSON")
