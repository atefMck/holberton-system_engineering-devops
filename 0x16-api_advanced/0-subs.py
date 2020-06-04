#!/usr/bin/python3
""" Python Script """
import requests


def number_of_subscribers(subreddit):
    """ Python Method """
    link = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'mechken.atef@gmail.com'
    }

    reddit_req = requests.get(link, headers=headers)
    reddit_info = reddit_req.json()
    try:
        subscribers = reddit_info["data"]["subscribers"]
        return subscribers
    except Exception as e:
        return 0
