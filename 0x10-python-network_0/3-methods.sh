#!/bin/bash
# Write a Bash script that takes in a URL and displays all HTTP methods
curl -sI "$1" | awk -F':' '/Allow/ {print $2}' | cut -d' ' -f2
