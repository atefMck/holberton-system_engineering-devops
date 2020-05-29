#!/usr/bin/python3
""" Python Script """
import json
import requests
from sys import argv

if __name__ == "__main__":
    u_link = "https://jsonplaceholder.typicode.com/users"
    file = 'todo_all_employees.json'

    u_info = requests.get("{}/".format(u_link)).json()
    data = dict()
    for user in u_info:
        uid = user['id']
        username = user['username']
        data[str(uid)] = []
        todo_info = requests.get("{}/{}/todos".format(u_link, uid)).json()
        for todo in todo_info:
            data[str(uid)].append(
                {
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": username
                }
            )

    with open(file, 'w', newline='') as jsonfile:
        json.dump(data, jsonfile)
