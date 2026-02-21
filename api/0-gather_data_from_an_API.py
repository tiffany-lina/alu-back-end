#!/usr/bin/python3
"""
Gather data from JSONPlaceholder API for a given employee ID
and display TODO list progress.
"""

import requests
import sys


def get_employee(employee_id):
    """Fetch employee info from API."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


def get_todos(employee_id):
    """Fetch TODO list for a given employee."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": employee_id})
    if response.status_code != 200:
        return []
    return response.json()


def display_progress(employee_id):
    """Display TODO list progress for the employee."""
    employee = get_employee(employee_id)
    if not employee:
        return

    todos = get_todos(employee_id)
    total = len(todos)
    done_tasks = [t for t in todos if t.get("completed")]
    done_count = len(done_tasks)

    # First line split for PEP8 (≤79 characters)
    print(
        "Employee {} is done with tasks({}/{})".format(
            employee["name"], done_count, total
        ) + ":"
    )

    for task in done_tasks:
        print("\t {}".format(task["title"]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        sys.exit("Employee ID must be an integer")

    display_progress(emp_id)
