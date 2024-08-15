#!/usr/bin/env python3
"""Takes the name of a subreddit and returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """
    Arguments:
    subreddit -- the name of the subreddit you want to check (string)

    Returns:
    int -- number of subscribers if successful, otherwise returns 0
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python:myapp:v1.0 (by /u/DYung06)',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return (response.json()["data"]["subscribers"])
    else:
        return (0)
