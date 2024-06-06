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
    user_agent = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    reddit = requests.get(url, headers=user_agent, allow_redirects=False)
    if reddit.status_code == 200:
        try:
            x = reddit.json()
            return (x.get("data", {}).get("subscribers"))
        except ValueError:
            return (0)
    else:
        return (0)
