#!/bin/bash
# adavnced #0
curl -o /dev/null -s -w "%{http_code}" $1
