#!/usr/bin/python3

"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    r = requests.get('https://api.github.com/user',
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
