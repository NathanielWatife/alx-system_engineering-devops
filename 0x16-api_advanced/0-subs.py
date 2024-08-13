#!/usr/bin/python3
"""
Module to query the Reddit API for the number of subscribers in a subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Function to get the number of subscribers for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.

    Returns:
    - int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check for a successful request
        if response.status_code == 200:
            data = response.json()
            return data['data'].get('subscribers', 0)
        
        # If the subreddit is invalid or not found
        return 0
    
    except Exception:
        return 0
