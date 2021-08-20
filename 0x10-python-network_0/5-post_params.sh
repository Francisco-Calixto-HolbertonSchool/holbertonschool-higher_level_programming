#!/bin/bash
# post request with variable changes
curl -sL -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST $1
