#!/usr/bin/python3
"""
Export employee TODO list data to JSON format.
"""

import json
import requests
import sys


def export_to_json(user_id):
    """Fetch user and todos, then export to JSON."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_response = requests.get(f"{base_url}/users/{user_id}")
    if user_response.status_code != 200:
        print(f"User {user_id} not found.")
        return
    user = user_response.json()
    username = user.get("username")

    # Fetch user's todos
    todos_response = requests.get(
        f"{base_url}/todos", params={"userId": user_id}
    )
    if todos_response.status_code != 200:
        print(f"Could not fetch todos for user {user_id}.")
        return
    todos = todos_response.json()

    # Build JSON dictionary
    json_data = {
        str(user_id): [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            } for todo in todos
        ]
    }

    # Write to JSON file
    filename = f"{user_id}.json"
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <user_id>")
        sys.exit(1)
    user_id_arg = sys.argv[1]
    export_to_json(user_id_arg)
