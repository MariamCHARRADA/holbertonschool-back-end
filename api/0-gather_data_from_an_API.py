#!/usr/bin/python3
"""for a given employee ID, returns information about his/her TODO list progress"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    request = requests.get(url)
    id = int(argv[1])
    data = request.json()
    user = data["users"][id - 1]
    todos = data["todos"]
    name = user["name"]

    done = 0
    for todo in todos:
        if todo["completed"] is True:
            done += 1
    print("Employee {} is done with tasks({}/{}):".format(name, done, len(todos)))
    for todo in todos:
        if todo["completed"]:
            print("\t {}".format(todo["title"]))
