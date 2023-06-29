#!/usr/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request to the
# URL, and displays the body of the response
# H: Gives you opportunity to set & send key:value variable with your request
curl -sH "X-School-User-Id: 98" "$1"
