#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[2]
    base_url = "https://jsonplaceholder.typicode.com/todos"
    
    try:
        user_response = requests.get(f"{base_url}users/{user_id}")
        user_response.raise_for_status()
        user = user_response.json()
        
        todos_response = requests.get(f"{base_url}todos", params={"userId": user_id})
        todos_response.raise_for_status()
        todos = todos_response.json()
        
        completed = [t.get("title") for t in todos if t.get("completed") is True]
        print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completed), len(todos)))
        [print("\t {}".format(c)) for c in completed]

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
