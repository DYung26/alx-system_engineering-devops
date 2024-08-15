#!/usr/bin/python3
"""Module to fetch and print the top ten hot posts of a given subreddit."""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the top ten hot posts for the specified subreddit.

    Arguments:
    subreddit -- the name of the subreddit you want to check (string)

    Returns:
    None -- prints "None" if the request fails or if there are no posts
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'python:myapp:v1.0 (by /u/DYung06)',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        hot_posts = response.json()["data"]["children"]
        for hot_post in hot_posts:
            print(hot_post["data"]["title"])
    else:
        print("None")
