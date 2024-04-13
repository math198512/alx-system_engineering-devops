#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
and export data in the JSON format.
"""

import json
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
    tasks = []
    for item in todos:
        task = {}
        task["task"] = item["title"]
        task["completed"] = item["completed"]
        task["username"] = user["username"]
        tasks.append(task)
    todos_dict = {f"{employee_id}": tasks}

    json_object = json.dumps(todos_dict)

    file_json = f"{employee_id}.json"

    with open(file_json, "w") as outfile:
        outfile.write(json_object)
