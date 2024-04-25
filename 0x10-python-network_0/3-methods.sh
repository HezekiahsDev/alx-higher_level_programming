#!/bin/bash
# this script will display all HTTP methods the server will accept in a URL

curl -sI "$1" | grep "Allow" | cut -d " " -f2-`
