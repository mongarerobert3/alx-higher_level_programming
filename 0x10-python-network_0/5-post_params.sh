#!/bin/bash
# Bash script that takes in a URL & displays the body of the response
curl -s "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
