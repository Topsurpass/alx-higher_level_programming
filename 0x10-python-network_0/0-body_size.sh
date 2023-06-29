#!/usr/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays
# the size of the body of the response
# -s : silent the progress meter of curl while making the request
# -I : It sends Head request to the server and retrieves only the header

# Method 1
# curl -sI "$1" | awk -F':' '/Content-Length/ {gsub(/^[ \t]+|[ \t]+$/, "", $2); print $2}'
# Method 2
#curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
# Method 3
curl -sI "$1" | awk -F':' '/Content-Length/ {print $2}' | cut -d' ' -f2
