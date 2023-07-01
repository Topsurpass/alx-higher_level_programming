#!/usr/bin/python3

"""
The Holberton School staff evaluates candidates applying for a back-end
position with multiple technical challenges, like this one:

Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”. You must use the GitHub API, here is the
documentation https://developer.github.com/v3/repos/commits/.
Print all commits by: `<sha>: <author name>` (one by line)
"""

import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    user = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo)

    r = requests.get(url)
    dic = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                dic[i].get('sha'), dic[i].get('commit').get(
                                                'author').get('name')))
    except IndexError:
        pass
