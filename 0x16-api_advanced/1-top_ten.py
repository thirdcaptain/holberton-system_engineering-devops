#!/usr/bin/python3
"""
queries Reddit and returns titles of first 10 hot posts
"""

import json
import requests


def top_ten(subreddit):
    """
    queries Reddit and returns titles of first 10 hot posts
    """
    title_list = []
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'user-agent': 'thirdcaptain'}

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False).json()
        child_list = response.get("data").get("children")
        for child in child_list:
            title_list.append(child.get("data").get("title"))

        for i in range(10):
            print(title_list[i])
    except Exception:
        print("None")
