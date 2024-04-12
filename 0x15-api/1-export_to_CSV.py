#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
and export data in the CSV format.
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
    params1 = {"userId": employee_id, "completed": "true"}
    completed_todos_res = get(url + "todos", params=params1)
    completed_todos = completed_todos_res.json()
    employee_name = user["name"]
    total_number_of_tasks = len(todos)
    number_of_done_tasks = len(completed_todos)
    file = f"{employee_id}.csv"
    with open(file, "w") as f:
        for item in todos:
            f.write('"{}","{}","{}","{}"\n'.format(
                employee_id,
                user["username"],
                item["completed"],
                item["title"]))
