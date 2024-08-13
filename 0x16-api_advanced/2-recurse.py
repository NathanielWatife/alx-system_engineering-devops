#!/usr/bin/python3
"""
Module to recursively query the Reddit API and return a list of titles of all hot articles for a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function to get all hot article titles for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.
    - hot_list (list): Accumulator for the titles of hot articles.
    - after (str): Parameter for pagination, representing the last article fetched.

    Returns:
    - list: A list containing the titles of all hot articles, or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.hot.recurse:v1.0 (by /u/yourusername)"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check for a successful request
        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            
            # Append the titles to the hot_list
            for post in posts:
                hot_list.append(post['data']['title'])
            
            # Recursively call the function if there are more posts
            after = data.get('after')
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None

    except Exception:
        return None
