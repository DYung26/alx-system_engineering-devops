#!/usr/bin/python3
"""
A script to fetch user data and their to-do list from the
JSONPlaceholder API, and write the data to a JSON file.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    base_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    r = requests.get(f'{base_url}/users/{user_id}/').json()
    r_todo = requests.get(f'{base_url}/users/{user_id}/todos').json()

    output_file = f"{user_id}.json"
    with open(output_file, 'w', newline='') as jsonfile:
        task_list = []

        for todo in r_todo:
            task_list.append({"task": f'{todo["title"]}',
                              "completed": f'{todo["completed"]}',
                              "username": f'{r["username"]}'})
        json_data = {f"{user_id}": task_list}
        json.dump(json_data, jsonfile)
