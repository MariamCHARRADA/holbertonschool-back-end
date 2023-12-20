#!/usr/bin/python3
"""for a given employee ID, returns information about his/her TODO list"""
import requests
from sys import argv

if __name__ == "__main__":
    
    id = int(argv[1])
    
    # Make requests to the API
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={id}")

    # Print status codes
    print(f"TODOs API Status Code: {todos_response.status_code}")

    
    url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    todos_response = requests.get(url)
    todos_data = todos_response.json()
    name = todos_data[0].get("username")

    done = 0
    for todo in todos_data:
        if todo["completed"] is True:
            done += 1
    print(
        "Employee {} is done with tasks({}/{}):".format(name, done, len(todos_data))
    )
    for todo in todos_data:
        if todo["completed"]:
            print("\t {}".format(todo["title"]))
