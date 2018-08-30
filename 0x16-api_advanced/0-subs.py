#!/usr/bin/python3
"""
queries Reddit and returns total number of subscribers
"""

import json
import requests


def number_of_subscribers(subreddit):
    """
    queries Reddit and returns total number of subscribers
    """
    url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    headers = {'user-agent': 'thirdcaptain'}

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False).json()
        child_list = response.get("data").get("children")
        first_child = child_list[0].get("data")
        subs = first_child.get("subreddit_subscribers")
        return subs
    except Exception:
        return 0
