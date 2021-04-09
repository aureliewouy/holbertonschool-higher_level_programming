#!/usr/bin/python3
""" Write a Python script that takes your GitHub credentials
and uses the GitHub API to display your id"""
import requests
import sys


if __name__ == "__main__":
    """code should not be executed when imported"""
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    response = requests.get(url).json()
    for r in response[:10]:
        print("{}: {}".format(r.get('sha'),
                              r.get('commit').get('author').get('name')))
