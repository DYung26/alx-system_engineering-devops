#!/usr/bin/python3
"""
Recursively fetches and counts the occurrences of specified words...
...in the titles of all hot posts of a subreddit.
"""
import requests


def cout_words(subreddit, word_list, hot_list, after=None):
    """
    Recursively fetches the titles of all hot posts for the specified subreddit
    and counts the occurrences of words from the word_list in the titles.

    Arguments:
    subreddit -- the name of the subreddit you want to check (string)
    word_list -- a list of words to count in the titles (list of strings)
    hot_list -- a list that stores the titles of the hot posts
      (default is an empty list)
    after -- a string indicating the "after" parameter used for pagination
             (default is None)

    Returns:
    None -- prints the count of each word in the word_list across all...
            hot post titles
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {
        'User-Agent': 'python:myapp:v1.0 (by /u/DYung06)',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        word_list = list(set(word_list))
        hot_posts = response.json()["data"]["children"]
        for hot_post in hot_posts:
            hot_list.append(hot_post["data"]["title"])
        after = response.json()["data"]["after"]
        count_words(subreddit, word_list, hot_list, after)
        for word in word_list:
            count = ' '.join(hot_list).count(word)
            print(f"{word}: {count}")
    else:
        print("")
