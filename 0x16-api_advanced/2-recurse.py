#!/usr/bin/python3
""" doc for module"""
import requests


def recurse(subreddit, hot_list=[] , after=""):
    """ doc for method"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Chrome/97.0.4692.71"}
    params = {"after": after}
    response = requests.get(url, allow_redirects=False, headers=headers,
                            params=params)
    all_posts = []
    if response.status_code == 200:
        data = response.json()
        after = data["data"]["after"]
        if after is None:
            return all_posts
        for post in data["data"]["children"]:
            all_posts.append(post["data"]["title"])
        next = recurse(subreddit, after)
        all_posts.extend(next)
        return all_posts
    return None
