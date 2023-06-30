#!/usr/bin/python3

"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.

info() returns a dictionary containing server response header details
"""

from urllib.request import urlopen
from sys import argv


with urlopen(argv[1]) as response:
    html = response.info()
    print(html['X-Request-Id'])
