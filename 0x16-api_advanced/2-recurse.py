#!/usr/bin/python3
"""
queries Reddit and returns titles of all hot articles
"""

import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    queries Reddit and returns titles of hot articles
    """
    url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    headers = {'user-agent': 'thirdcaptain'}
    try:
        """after"""
        response = requests.get(url,
                                headers=headers,
                                allow_redirects=False,
                                params={'after': after}).json()
        after = response.get("data").get("after")
        child_list = response.get("data").get("children")

        for child in child_list:
            hot_list.append(child.get("data").get("title"))

        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list

    except Exception:
        return (None)
