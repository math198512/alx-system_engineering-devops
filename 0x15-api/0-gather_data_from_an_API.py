#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = argv[1]
    employee_res = get(url + "users/{}".format(employee_id))
    user = employee_res.json()
    params = {"userId": employee_id}
    todos_res = get(url + "todos", params=params)
    todos = todos_res.json()
    employee_name = user["name"]
    total_number_of_tasks = len(todos)
    print("Employee {} is done with tasks(NUMBER_OF_DONE_TASKS/{})".format(employee_name, total_number_of_tasks))
