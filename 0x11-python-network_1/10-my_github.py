#!/usr/bin/python3
"""display GitHub credentials using API
Usage: ./10-my_github.py <GitHub username> <GitHub password>
"""


import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))
