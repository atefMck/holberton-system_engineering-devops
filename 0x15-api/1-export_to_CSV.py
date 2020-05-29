#!/usr/bin/python3
""" Python Script """
import csv
import requests
from sys import argv

if __name__ == "__main__":
    u_link = "https://jsonplaceholder.typicode.com/users"
    uid = argv[1]

    u_info = requests.get("{}/{}".format(u_link, uid)).json()
    username = u_info['username']

    todo_info = requests.get("{}/{}/todos".format(u_link, uid)).json()
    done = list()
    with open('USER_ID.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quoting=csv.QUOTE_ALL)
        for todo in todo_info:
            status = todo['completed']
            title = todo['title']
            writer.writerow([uid, username, status, title])
