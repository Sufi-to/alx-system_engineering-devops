#!/usr/bin/python3
"""Script using a given REST API to get data back."""
from sys import argv
import json
import requests as req


def tasks_done(id):
    """Calculate the number of completed tasks."""
    url = "https://jsonplaceholder.typicode.com/todos"
    res = req.get(url).text
    obj = json.loads(res)
    tasks_done = []
    count = 0
    for i in obj:
        if i['userId'] == id and i['completed']:
            count += 1
            tasks_done.append(i['title'])
    return count, tasks_done


if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    res = req.get(url).text
    obj = json.loads(res)

    num_task, comp_tasks = tasks_done(obj['id'])
    print(f"Employee {obj['name']} is done with tasks({num_task}/20):")
    for i in comp_tasks:
        print("/t {}".format(i))
