#!/bin/bash
#sends a request to the url and display the size of the body
curl -sI "$1" | grep -i content-length | awk '{print $2}'
