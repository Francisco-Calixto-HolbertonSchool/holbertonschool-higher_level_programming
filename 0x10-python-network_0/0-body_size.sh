#!/bin/bash
# takes in a URL, sends a request to that URL, displays the size response
curl -s 0.0.0.0:5000 | wc -c
