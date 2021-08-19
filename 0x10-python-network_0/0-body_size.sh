#!/bin/bash
# takes in a URL, sends a request to that URL, displays the size response
curl -sI 0.0.0.0:5000 | awk '/Content-Length/ { print $2 }'
