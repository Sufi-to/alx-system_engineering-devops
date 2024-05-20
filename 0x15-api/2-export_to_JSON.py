#!/usr/bin/python3
"""Script to export data in the JSON format."""
import json
import requests as req
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = req.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = req.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{"task": todo.get("title"), "completed": todo.get(
            "completed"), "username": username} for todo in todos]}, jsonfile)
