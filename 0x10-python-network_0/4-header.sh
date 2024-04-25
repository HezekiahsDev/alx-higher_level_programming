#!/bin/bash
# this script will, send a GET request to the URL (taken in as an argument),
# and displays the body of the response

curl "$1" -sX GET -H "X-HolbertonSchool-User-Id:98"
