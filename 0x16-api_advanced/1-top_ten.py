#!/usr/bin/python3
""" Python Script """
import requests


def top_ten(subreddit):
    """ Python Method """
    link = "https://api.reddit.com/r/{}/hot".format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'mechken.atef@gmail.com'
    }

    reddit_req = requests.get(link, headers=headers)
    reddit_info = reddit_req.json()
    try:
        top_threads = reddit_info["data"]["children"][:10]
        for thread in top_threads:
            print(thread["data"]["title"])
    except Exception as e:
        print("None")
