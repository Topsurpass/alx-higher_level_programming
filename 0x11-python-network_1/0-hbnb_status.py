#!/usr/bin/python3
"""
Script that fetch https://intranet.hbtn.io/status and display response
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as r:
        html = r.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
