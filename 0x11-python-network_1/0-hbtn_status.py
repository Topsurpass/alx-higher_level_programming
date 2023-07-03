#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        page_body = response.read()
        print("Body response:")
        print("\t- type:", type(page_body))
        print("\t- content:", page_body)
        print("\t- utf8 content:", page_body.decode('utf-8'))
