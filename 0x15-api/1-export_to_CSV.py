#!/usr/bin/python3
"""
A script to fetch user data and their to-do list from the
JSONPlaceholder API, and write the data to a CSV file.
"""

if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys

    base_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    r = requests.get(f'{base_url}/users/{user_id}/').json()
    r_todo = requests.get(f'{base_url}/users/{user_id}/todos').json()

    output_file = f"{user_id}.csv"
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)

        for todo in r_todo:
            writer.writerow([
                f'{user_id}',
                f'{r["username"]}',
                f'{"True" if todo["completed"] else "False"}',
                f'{todo["title"]}'
                ])
