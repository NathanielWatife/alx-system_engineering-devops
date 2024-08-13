#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the first 10 hot posts for a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Function to print the titles of the first 10 hot posts for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.

    Prints:
    - Titles of the first 10 hot posts, or "None" if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.top.ten:v1.0 (by /u/yourusername)"}
    params = {"limit": 10}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check for a successful request
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            # Print the titles of the first 10 hot posts
            for post in posts:
                print(post['data']['title'])
        else:
            print("None")
    
    except Exception:
        print("None")
