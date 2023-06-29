#!/bin/bash
# Bash script that sends a request to a URL passed as an argument
curl -o /dev/null -w '%{http_code}' -sIL "$1"
