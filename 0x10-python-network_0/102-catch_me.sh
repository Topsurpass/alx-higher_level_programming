#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes server to respond
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
