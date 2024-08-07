#!/usr/bin/python3
"""
This script returns information about an employee's TODO list progress
It requires an employee ID to do that
"""


import requests
import sys


def fetch_employee_name(employee_id):
    """Fetch employee name by ID."""
    response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    response.raise_for_status()
    return response.json().get('name')


def fetch_todos(employee_id):
    """Fetch TODOs for a given employee ID."""
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos',
                            params={'userId': employee_id})
    response.raise_for_status()
    return response.json()


def main(employee_id):
    """Print TODO list progress for the given employee ID."""
    name = fetch_employee_name(employee_id)
    todos = fetch_todos(employee_id)
    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    print(f'Employee {name} is done with tasks({done_tasks}/{total_tasks}):')
    for task in completed_tasks:
        print(f'\t {task}')


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./todo_progress.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    main(employee_id)
