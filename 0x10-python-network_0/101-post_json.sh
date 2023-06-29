#!/usr/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first
# argument, and displays the body of the response.
# @ symbol tells curl to treat the argument that follows as a file and use
# its contents as the data for the request body.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
