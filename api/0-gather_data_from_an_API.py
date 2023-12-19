#!/usr/bin/python3
"""for a given employee ID, returns information about his/her TODO list"""
import requests
from sys import argv

if __name__ == "__main__":
    id = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    request = requests.get(f"{url}users/{id}")
    data = request.json()
    name = data["name"]
    todos = data["todos"]

    done = 0
    for todo in todos:
        if todo["completed"] is True:
            done += 1
    print(
        "Employee {} is done with tasks({}/{}):".format(name,
                                                        done,
                                                        len(todos)))
    for todo in todos:
        if todo["completed"]:
            print("\t {}".format(todo["title"]))
