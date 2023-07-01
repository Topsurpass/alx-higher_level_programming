#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        the_head = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(the_head)))
        print("\t- content: {}".format(the_head))
        print("\t- utf8 content: {}".format(the_head.decode('utf-8')))
