#!/usr/bin/python3
"""
Export all employees' TODO list data to a JSON file.

Format:
{
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE",
         "completed": TASK_COMPLETED_STATUS},
        ...
    ],
    ...
}
"""

import json
import requests


def fetch_all_users():
    """Fetch all users from the API and return as a list."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_todos_for_user(user_id):
    """Fetch all todos for a given user ID."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": user_id})
    response.raise_for_status()
    return response.json()


def export_all_todos_to_json(filename="todo_all_employees.json"):
    """Fetch todos for all users and export to a JSON file."""
    all_users = fetch_all_users()
    all_data = {}

    for user in all_users:
        user_id = str(user["id"])
        username = user["username"]
        todos = fetch_todos_for_user(user_id)
        all_data[user_id] = [
            {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            for todo in todos
        ]

    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(all_data, json_file)


if __name__ == "__main__":
    export_all_todos_to_json()
