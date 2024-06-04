#!/usr/bin/python3
"""
Script that queries the reddit api and prints the titles of
the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    payload = {"limit": 9}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    yo = requests.get(url, params=payload, allow_redirects=False)
    if yo.status_code == 200:
        x = yo.json()
        posts = x.get("data", {}).get("children", [])
        hel = [post.get("data", {}).get("title", []) for post in posts]
        for i in hel:
            print(i)
    else:
        print("None")
