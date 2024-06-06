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
    user_agent = {
        "User-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0"
        }
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    reddit = requests.get(url, headers=user_agent, allow_redirects=False)
    if reddit.status_code == 200:
        x = reddit.json()
        return (x.get("data", {}).get("subsribers"))
    else:
        return (0)
