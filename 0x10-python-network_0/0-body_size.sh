#!/bin/bash
# This script take a URL, send a request to display the size of resbonse body
# URL is stored in $1
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
