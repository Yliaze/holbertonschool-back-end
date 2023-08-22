#!/usr/bin/python3
"""Script that, using a REST API, retrieves TODO list progress
for a given employee ID and export data in the JSON format
(list of dictionaries)"""


import json
import requests
import sys

if len(sys.argv) > 2:
    print("Usage: python script_name.py employee_id")
    sys.exit(1)

"""URL of employees"""
employee_url = f"https://jsonplaceholder.typicode.com/users"

"""Send a GET request to get employee information"""
employee_response = requests.get(employee_url)
if employee_response.status_code != 200:
    print(f"Failed to retrieve employee data. \
    Status code: {employee_response.status_code}")
    sys.exit(1)
employee_data = employee_response.json()

"""Create a dictionary to store tasks for each user"""
json_dict_of_dict = {}

for employee in employee_data:
    employee_id = employee['id']

    """URL of employee's tasks"""
    todos_url = f"https://jsonplaceholder.typicode.com/\
todos?userId={employee_id}"

    """Send a GET request to get employee's TODO list"""
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to retrieve TODO data. \
        Status code: {todos_response.status_code}")
        sys.exit(1)
    todos_data = todos_response.json()

    """For loop to find tasks"""
    tasks_list = []
    for task in todos_data:
        task_data = {
            "username": employee['username'],
            "task": task['title'],
            "completed": task['completed'],
        }
        tasks_list.append(task_data)

    """Add tasks_list to the dictionary with employee_id as key"""
    json_dict_of_dict[employee_id] = tasks_list

"""Open and write in the JSON format"""
json_filename = f"todo_all_employees.json"
with open(json_filename, "w", newline='') as json_file:
    json.dump(json_dict_of_dict, json_file)
