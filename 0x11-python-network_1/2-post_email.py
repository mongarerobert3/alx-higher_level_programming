#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""

import urllib.request as request
import urllib.parse
import sys
from urllib import error


if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
