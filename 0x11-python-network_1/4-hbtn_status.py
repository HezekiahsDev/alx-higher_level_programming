#!/usr/bin/python3
""" request from https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    fetch_req = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(fetch_req.text)))
    print("\t- content: {}".format(r.text))
