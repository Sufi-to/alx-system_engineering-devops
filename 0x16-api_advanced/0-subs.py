#!/usr/bin/python3
"""
Script the queries the Reddit api and return the number of subscribers.
(not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Get the number of subscribers."""
    reddit = requests.get("https://www.reddit.com/r/{}/about.json".format(
        subreddit), allow_redirects=False)
    if reddit.status_code == 200:
        x = reddit.json()
        return (x['data']['subscribers'])
    return (0)
