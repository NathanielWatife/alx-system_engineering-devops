#!/usr/bin/python3
"""
Module to recursively query the Reddit API and count occurrences of given keywords in hot articles.
"""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursive function to count occurrences of keywords in hot article titles for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.
    - word_list (list): List of keywords to count.
    - after (str): Parameter for pagination, representing the last article fetched.
    - word_count (dict): Dictionary to store keyword counts.

    Prints:
    - Sorted counts of keywords in the specified format.
    """
    if word_count is None:
        word_count = {}

    # Convert word_list to lowercase
    word_list = [word.lower() for word in word_list]

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.keyword.counter:v1.0 (by /u/yourusername)"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check for a successful request
        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            
            # Process each post title
            for post in posts:
                title = post['data']['title'].lower()
                words = title.split()

                # Count occurrences of each keyword
                for word in word_list:
                    word_count[word] = word_count.get(word, 0) + words.count(word)

            # Recursively call the function if there are more posts
            after = data.get('after')
            if after is not None:
                return count_words(subreddit, word_list, after, word_count)
            else:
                # Sort and print the results
                sorted_keywords = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
                for keyword, count in sorted_keywords:
                    if count > 0:
                        print(f"{keyword}: {count}")

    except Exception:
        return None
