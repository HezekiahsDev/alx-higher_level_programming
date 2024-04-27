#!/usr/bin/python3
"""show 10 receent commits on GitHub
Usage: ./100-github_commits.py <repository name> <repository owner>
"""


import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commits_req = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits_req[i].get("sha"),
                commits_req[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
