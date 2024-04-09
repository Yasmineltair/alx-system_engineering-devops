i!/usr/bin/python3
""" doc for module"""


def number_of_subscribers(subreddit):
    """ doc for method"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Chrome/97.0.4692.71"}
    response = request.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
