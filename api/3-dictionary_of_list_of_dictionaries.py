#!/usr/bin/python3
"""for a given employee ID, returns information about his/her TODO list"""
import json
import requests



if __name__ == "__main__":


    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    name = user_data["name"]
    username = user_data["username"]

    filename = "todo_all_employees.json"
    todo_list = []
    for todo in todos_data:
        task_info = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": username,
        }
        todo_list.append(task_info)
    with open(filename, "w") as f:
        json.dump({id: todo_list}, f)
