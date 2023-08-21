#!/usr/bin/python3
"""Script that, using a REST API, retrieves TODO list progress
for a given employee ID"""


import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script_name.py employee_id")
    sys.exit(1)

"""Get the employee ID from the command-line argument"""
employee_id = sys.argv[1]

employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

"""Send a GET request to get employee information"""
employee_response = requests.get(employee_url)
if employee_response.status_code != 200:
    print(f"Failed to retrieve employee data. \
    Status code: {employee_response.status_code}")
    sys.exit(1)
employee_data = employee_response.json()

"""Send a GET request to get employee's TODO list"""
todos_response = requests.get(todos_url)
if todos_response.status_code != 200:
    print(f"Failed to retrieve TODO data. \
    Status code: {todos_response.status_code}")
    sys.exit(1)
todos_data = todos_response.json()

"""Count total and completed tasks"""
total_tasks = len(todos_data)
completed_tasks = 0
for task in todos_data:
    if task['completed']:
        completed_tasks += 1

"""Print employee's progress"""
print(f"Employee {employee_data['name']} \
is done with tasks({completed_tasks}/{total_tasks}):")

"""Print titles of completed tasks"""
for task in todos_data:
    if task['completed']:
        print(f"\t {task['title']}")
