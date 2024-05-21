#!/usr/bin/python3
"""
A script to fetch user data and their to-do lists from the
JSONPlaceholder API, and write the data to a JSON file.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    base_url = 'https://jsonplaceholder.typicode.com/'
    r = requests.get(f'{base_url}/users/').json()
    json_data = {}
    output_file = "todo_all_employees.json"
    task_list = []

    for user in r:
        user_id = user["id"]
        username = user["username"]
        r_todo = requests.get(f'{base_url}/users/{user_id}/todos').json()
        task_dict = {}

        for todo in r_todo:
            task = todo["title"]
            status = todo["completed"]

            task_dict.update({"username": username,
                              "task": task,
                              "completed": status
                              })
        task_list.append(task_dict)
        json_data.update({f"{user_id}": task_list})
    with open(output_file, 'w', newline='') as jsonfile:
        json.dump(json_data, jsonfile)
