#!/bin/bash
# This script take a URL, send a request to display the size of resbonse body
# URL is stored in $1

curl -s "$1" | wc -c
