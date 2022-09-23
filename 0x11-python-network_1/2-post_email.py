#!/usr/bin/python3
"""
Python script that takes in a URL, sends a POST request to the passed URL 
with the email as a parameter, and displays the body of the response
 """
import urllib.request as request
import sys


if __name__ == "__main__":
    data = request.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        html = response.read()
        print('{}'.format(html.decode('utf-8')))
