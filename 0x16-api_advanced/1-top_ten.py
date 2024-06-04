#!/usr/bin/python3
"""
Script that queries the reddit api and prints the titles of
the first 10 hot posts listed for a given subreddit
"""
import requests


# def top_ten(subreddit):
payload = {"where": "popular"}
yo = requests.get("https://www.reddit.com/r/programming.json", params=payload, allow_redirects=False)
x = yo.json()
print(x)
