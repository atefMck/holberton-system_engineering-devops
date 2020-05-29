#!/usr/bin/python3
""" Python Script """
import JSON
import requests
from sys import argv

if __name__ == "__main__":
    u_link = "https://jsonplaceholder.typicode.com/users"
    uid = argv[1]

    u_info = requests.get("{}/{}".format(u_link, uid)).json()
    username = u_info['username']
    todo_info = requests.get("{}/{}/todos".format(u_link, uid)).json()
    done = list()
    file = '{}.json'.format(uid)
    data = dict()
    for todo in todo_info:
        data[str(uid)] = [
            {
                "task": todo['title'],
                "completed": todo['completed']
                "username": todo['username']
            }
        ]

    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quoting=csv.QUOTE_ALL)
