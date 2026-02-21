#!/usr/bin/python3
"""
This script retrieves the TODO list progress of a given employee
from the JSONPlaceholder REST API.
"""

import requests
import sys


def fetch_employee_todos(employee_id):
    """Fetch employee info and TODO list using the REST API."""
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    response_user = requests.get(user_url)
    if response_user.status_code != 200:
        return None, None, None, None

    user = response_user.json()
    employee_name = user.get("name")

    response_todos = requests.get(todos_url)
    todos = response_todos.json()

    done_tasks = [t.get("title") for t in todos if t.get("completed")]
    total_tasks = len(todos)
    done_count = len(done_tasks)

    return employee_name, done_tasks, done_count, total_tasks


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer")
        sys.exit(1)

    employee_name, done_tasks, done_count, total_tasks = fetch_employee_todos(employee_id)
    if not employee_name:
        print("Employee not found")
        sys.exit(1)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_count, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    main()
