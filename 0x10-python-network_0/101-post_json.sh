#!/bin/bash
# json post
curl -s -H "content-type: application/json" -d @"$2" $1
