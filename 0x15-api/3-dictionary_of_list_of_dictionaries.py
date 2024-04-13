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
    employees_res = get(url + "users")
    users = employees_res.json()
    num_users = len(users)
    all_users = {}
    for i in range(num_users):
        user_id = i + 1
        todos_res = get(url + "todos", params={"userId": user_id})
        todos = todos_res.json()
        tasks = []
        for item in todos:
            task = {}
            task["username"] = users[i]["username"]
            task["task"] = item["title"]
            task["completed"] = item["completed"]
            tasks.append(task)
        all_users[f"{user_id}"] = tasks

    json_object = json.dumps(all_users)

    file_json = "todo_all_employees.json"

    with open(file_json, "w") as outfile:
        outfile.write(json_object)
