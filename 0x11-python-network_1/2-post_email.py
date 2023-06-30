#!/usr/bin/python3

"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv


values = {'email': argv[2]}

data = urlencode(values)
data = data.encode('ascii')
req = Request(argv[1], data)
with urlopen(req) as response:
    the_email = response.read().decode('utf-8')
    print(the_email)
