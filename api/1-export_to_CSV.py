#!/usr/bin/python3
"""
Exports all TODO tasks of a given employee to a CSV file.

Format:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

File name:
USER_ID.csv

Usage:
    ./1-export_to_CSV.py EMPLOYEE_ID
"""

import csv
import requests
import sys


def fetch_employee_data(employee_id):
    """Fetch employee info and all TODOs from the JSONPlaceholder API."""
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )

    response_user = requests.get(user_url)
    if response_user.status_code != 200:
        return None, None

    user = response_user.json()
    username = user.get("username")

    response_todos = requests.get(todos_url)
    if response_todos.status_code != 200:
        return username, []

    todos = response_todos.json()
    return username, todos


def export_to_csv(employee_id, username, todos):
    """Export all tasks to a CSV file named USER_ID.csv."""
    filename = "{}.csv".format(employee_id)
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            completed = task.get("completed", False)
            title = task.get("title", "")
            writer.writerow([employee_id, username, completed, title])


def main():
    """Main execution."""
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer")
        sys.exit(1)

    username, todos = fetch_employee_data(employee_id)
    if username is None:
        print("Employee not found")
        sys.exit(1)

    export_to_csv(employee_id, username, todos)


if __name__ == "__main__":
    main()
