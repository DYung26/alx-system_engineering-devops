#!/usr/bin/python3
"""
Recursively fetches and prints the titles of all hot posts of a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches the titles of all hot posts...
    ...for the specified subreddit.

    Arguments:
    subreddit -- the name of the subreddit you want to check (string)
    hot_list -- a list that stores the titles of the hot posts
                (default is an empty list)
    after -- a string indicating the "after" parameter used for pagination
             (default is None)

    Returns:
    hot_list -- a list containing the titles of all hot posts if successful
    None -- returns None if the request fails or if there are no posts
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {
        'User-Agent': 'python:myapp:v1.0 (by /u/DYung06)',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        hot_posts = response.json()["data"]["children"]
        for hot_post in hot_posts:
            hot_list.append(hot_post["data"]["title"])
        after = response.json()["data"]["after"

        recurse(subreddit, hot_list, after)
    else:
        return None
    return hot_list
