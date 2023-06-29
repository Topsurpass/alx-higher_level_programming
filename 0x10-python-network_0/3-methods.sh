#!/bin/bash
# Write a Bash script that takes in a URL and displays all HTTP methods
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '
