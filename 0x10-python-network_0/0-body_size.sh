#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays
curl -sI "$1" | awk -F':' '/Content-Length/ {print $2}' | cut -d' ' -f2
