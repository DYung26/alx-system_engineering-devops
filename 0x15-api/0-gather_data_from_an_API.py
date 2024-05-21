#!/usr/bin/python3
"""
A script to fetch and display the number of completed tasks for a given user
from the JSONPlaceholder API.
The script takes a user ID as a command-line argument and retrieves the user's
details and their to-do list.
It then counts the number of completed tasks and prints them along with the
task titles.
"""

if __name__ == '__main__':
    import json
    import requests
    import sys

    base_url = 'https://jsonplaceholder.typicode.com/'
    r = requests.get(f'{base_url}/users/{sys.argv[1]}/').json()
    r_todo = requests.get(f'{base_url}/users/{sys.argv[1]}/todos').json()

    done_t = 0
    for todo in r_todo:
        if todo["completed"]:
            done_t += 1

    print(f'Employee {r["name"]} is done with tasks({done_t}/{len(r_todo)}):')
    for todo in r_todo:
        if todo["completed"]:
            print(f'\t {todo["title"]}')
