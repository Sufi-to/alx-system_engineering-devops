#!/usr/bin/python3
"""Script that counts the number of give words occurrences in the hot titles"""
import requests
from requests import get


def count_words(subreddit, word_list, after="", w_dic={}):
    """Returns the word counts."""
    red = "https://www.reddit.com/r/"
    headers = {'user-agent': 'my-agent'}
    if not w_dic:
        for word in word_list:
            w_dic[word] = 0

    if after is None:
        word_list = [[key, value] for key, value in w_dic.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for w in word_list:
            if w[1]:
                print("{}: {}".format(w[0].lower(), w[1]))
        return None
    url = red + "{}/hot/.json".format(subreddit)
    p = {'limit': 100, 'after': after}
    fr = get(url, headers=headers, params=p, allow_redirects=False)
    if fr.status_code != 200:
        return None
    try:
        js = fr.json()
    except ValueError as e:
        return None
    try:

        data = js.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            title = post.get("title")
            lower = [s.lower() for s in title.split(' ')]

            for w in word_list:
                w_dic[w] += lower.count(w.lower())

    except requests.RequestException as er:
        return None

    count_words(subreddit, word_list, after, w_dic)
