#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
