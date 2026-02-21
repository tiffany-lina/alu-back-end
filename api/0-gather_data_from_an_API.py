#!/usr/bin/python3
"""
Gather data from JSONPlaceholder API for a given employee ID
and display TODO list progress.
"""

import sys
import requests


def get_employee_data(employee_id):
    """Fetch employee information from API."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_employee_todos(employee_id):
    """Fetch TODO list for the employee from API."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": employee_id})
    response.raise_for_status()
    return response.json()


def display_todo_progress(employee_id):
    """Display employee TODO progress in the required format."""
    employee = get_employee_data(employee_id)
    todos = get_employee_todos(employee_id)

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task["completed"]]
    num_done = len(done_tasks)

    # First line
    print(
        f"Employee {employee['name']} is done with tasks("
        f"{num_done}/{total_tasks}):"
    )

    # Completed task titles
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Usage:\npython3 0-gather_data_from_an_API.py "
            "<employee_id>"
        )
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    display_todo_progress(emp_id)
