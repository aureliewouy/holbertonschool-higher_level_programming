#!/usr/bin/python3
""" Write a Python script that takes your GitHub credentials
and uses the GitHub API to display your id"""
import requests
import sys


if __name__ == "__main__":
    """code should not be executed when imported"""
    usrname = sys.argv[1]
    passwd = sys.argv[2]
    url = "https://api.github.com/user"
    info = {'Authorization': 'token {}'.format(passwd)}
    r = requests.get(url, headers=info).json()
    if r.get('id'):
        print("{}".format(r.get('id')))
    else:
        print("None")
