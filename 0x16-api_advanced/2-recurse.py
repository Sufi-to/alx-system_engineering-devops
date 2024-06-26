#!/usr/bin/python3
"""
Script that queries the Reddit API and returns a list containing the titles of
all hot articles for a given subreddit. If no results are found for the given
subreddit, the function should return None.
"""
import requests


def recurse(subreddit, after=None, hot_list=None):
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after} if after else {}
    response = requests.get(url, params=params, allow_redirects=False)
    if response.status_code == 200:
        x = response.json()
        posts = x.get("data", {}).get("children", [])
        hot_list.extend([post["data"]["title"] for post in posts])
        after = x.get("data", {}).get("after")
        if after:
            return recurse(subreddit, after, hot_list)
        else:
            return hot_list
    else:
        return None
