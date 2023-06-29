#!/usr/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first
# argument and displays the body of the response
# X: When used, u can type in directly the http method you want
curl -sX DELETE "$1"
