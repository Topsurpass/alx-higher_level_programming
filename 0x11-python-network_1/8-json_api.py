#!/usr/bin/python3

"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":

    if len(argv) < 2:
        arg = ""
    else:
        arg = argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': arg})

    try:
        dic = r.json()
        if dic:
            print("[{}] {}".format(dic['id'], dic['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
