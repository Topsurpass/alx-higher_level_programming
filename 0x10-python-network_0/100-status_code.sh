#!/usr/bin/bash
# Bash script that sends a request to a URL passed as an argument, and
# displays only the status code of the response.
# Placeholders: http_code, content_length, content_type, time_connect e.t.c

curl -o /dev/null -w '%{http_code}' -sIL "$1"
