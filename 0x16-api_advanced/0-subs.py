#!/usr/bin/python3
"""
Script the queries the Reddit api and return the number of subscribers.
(not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Get the number of subscribers."""
    if subreddit is None or type(subreddit) is not str:
        return 0
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    reddit = requests.get(url, headers=headers, allow_redirects=False)
    if reddit.status_code == 200:
        x = reddit.json()
        return (x.get("data", {}).get("subsribers"))
    else:
        return (0)
