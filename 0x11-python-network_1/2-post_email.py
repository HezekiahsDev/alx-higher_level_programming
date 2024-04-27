#!/usr/bin/python3
"""POST request: email to a url
Useage: ./2-post_email.py <URL> <email>
"""


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    demail = urllib.parse.urlencode(val).encode("ascii")

    req = urllib.request.Request(url, demail)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
