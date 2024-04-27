#!/usr/bin/python3
"""find a given letter http://0.0.0.0:5000/search_user
Usage: ./8-json_api.py <letter>
"""


import sys
import requests


if __name__ == "__main__":
    txt_search = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": text_search}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
