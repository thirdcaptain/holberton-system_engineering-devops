#!/usr/bin/python3
"""
Gathers information from https://jsonplaceholder.typicode.com/ RESTFUL API
Takes in a given employee ID, returns information about TODO list progress
"""

if __name__ == "__main__":
    import sys
    import requests
    import json

    userId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_get = "/users?id=" + userId
    todo_get = "/todos?userId=" + userId
    resp_user = requests.get(base_url + user_get)
    resp_todo = requests.get(base_url + todo_get)
    user_json = resp_user.json()
    todo_json = resp_todo.json()
    done_tasks = 0
    total_tasks = 0

    for user in user_json:
        user_name = user.get("name")

    for todo in todo_json:
        total_tasks = total_tasks + 1
        if todo.get("completed") is True:
            done_tasks = done_tasks + 1

    print(user_name)
    print(total_tasks)
    print(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                          done_tasks,
                                                          total_tasks))
    for todo in todo_json:
        if todo.get("completed") is True:
            print("\t {}".format(todo.get("title")))
