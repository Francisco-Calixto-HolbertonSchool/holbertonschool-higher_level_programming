#!/bin/bash
# takes in a URL, sends a request to that URL, displays the size response
curl -s $1 | wc -c
