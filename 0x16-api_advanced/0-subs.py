#!/usr/bin/python3
import requests
"""
    function that queries the Reddit API 
"""

def number_of_subscribers(subreddit):
    '''return number subscribers'''
    try:
        r = requests.get('https://www.reddit.com/r/{}/about.json'.
                         format(subreddit),
                         headers={'User-Agent': 'custom'},
                         allow_redirects=False)
        return r.json().get('data').get('subscribers')     
    except:
        return 0
