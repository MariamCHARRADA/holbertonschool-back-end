#!/usr/bin/python3
"""for a given employee ID, returns information about his/her TODO list"""
import requests
from sys import argv
import csv

if __name__ == "__main__":
    id = int(argv[1])

    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    name = user_data["name"]
    username = user_data["username"]

    done = 0
    for todo in todos_data:
        if todo["completed"] is True:
            done += 1
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          done,
                                                          len(todos_data)))
    for todo in todos_data:
        if todo["completed"]:
            print("\t {}".format(todo["title"]))
    
    filename = f"{id}.csv"
    field_names = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        for todo in todos_data:
            user_info = {
                'USER_ID': id,
                'USERNAME': username,
                'TASK_COMPLETED_STATUS': todo['completed'],
                'TASK_TITLE': todo['title']
            }
            writer.writerows([user_info])
