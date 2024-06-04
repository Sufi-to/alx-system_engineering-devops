#!/usr/bin/python3
"""
Script the queries the Reddit api and return the number of subscribers.
(not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Get the number of subscribers."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    reddit = requests.get(url, allow_redirects=False)
    if reddit.status_code == 200:
        x = reddit.json()
        return (x.get("data", {}).get("subsribers"))
    else:
        return (0)
