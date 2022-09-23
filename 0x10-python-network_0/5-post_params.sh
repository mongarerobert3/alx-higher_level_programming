#!/bin/bash
# POST request and displays the body of the response
curl "$1" -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
