#!/usr/bin/python3
"""
This script returns information about an employee's TODO list progress
It requires an employee ID to do that
Added functionality to import all employee data
"""


import json
import requests
import sys


def fetch_all_employees():
    """Fetch all the employees"""
    response = requests.get(f'https://jsonplaceholder.typicode.com/users')
    response.raise_for_status()
    return response.json()


def fetch_todos(employee_id):
    """Fetch all TODOs for a given employee ID."""
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos',
                            params={'userId': employee_id})
    response.raise_for_status()
    return response.json()


def export_to_json(all_employees_data):
    """Export all employee TODO list data to JSON."""
    filename = 'todo_all_employees.json'
    try:
        with open(filename, 'w') as file:
            json.dump(all_employees_data, file, indent=4)
    except IOError as e:
        print(f'Error writing to file {filename}: {e}')


def main():
    """Fetch all TODOs for all employees and export data to JSON."""
    employees = fetch_all_employees()
    all_employees_data = {}

    for employee in employees:
        employee_id = employee.get('id')
        username = employee.get('username')
        todos = fetch_todos(employee_id)

        all_employees_data[str(employee_id)] = [
                {
                    'username': username,
                    'task': todo['title'],
                    'completed': todo['completed']
                }
                for todo in todos
            ]

        export_to_json(all_employees_data)


if __name__ == "__main__":
    main()
