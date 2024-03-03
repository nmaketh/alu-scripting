#!/usr/bin/python3
"""" Top Ten Limit"""

import requests


def top_ten(subreddit):
    """"top ten"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10" \
        .format(subreddit)

    res = requests.get(url,
                       headers={
                           'User-Agent': 'Mozilla/5.0'})

    if res.status_code != 200:
        print(None)
    else:
        json_response = res.json()
        posts = json_response.get('data').get('children')
        [print(post.get('data').get('title')) for post in posts]usr/bin/python3




"""print the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        HOT_POSTS = RESPONSE.json().get("data").get("children")
        [print(post.get('data').get('title')) for post in HOT_POSTS]
    except Exception:
        print(None)
