#!/usr/bin/python3
"""
Script the queries the Reddit api and return the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    yo = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json")
    if yo.status_code == 200:
        x = yo.json()
        return (x['data']['subscribers'])
    return (0)
