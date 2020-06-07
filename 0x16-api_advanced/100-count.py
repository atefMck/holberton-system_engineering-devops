#!/usr/bin/python3
""" Python module """
import re
import requests


def count_words(subreddit, word_list, after='', occurs={}):
    """ Python method """
    url = 'https://api.reddit.com/r/' + subreddit + '?limit=100&after=' + after
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'mechken.atef@gmail.com'
    }
    response = requests.get(url, headers=headers)
    try:
        data = response.json()
    except:
        return
    if (str(response.status_code) == '404'):
        return
    dataLength = len(data['data']['children'])
    if (dataLength is 0):
        return
    for i in range(0, dataLength):
        try:
            get_title = data['data']['children'][i]['data']['title']
            for a in word_list:
                try:
                    occurs[a]
                except KeyError:
                    occurs[a] = 0
                finally:
                    occurs[a] += re.subn(r'(?i)(?<!\S)\b{}\b(?!\S)'.format(a),
                                         '', get_title)[1]
        except:
            pass
    afterVal = data['data']['after']
    if (afterVal is not None):
        return count_words(subreddit, word_list, afterVal, occurs)
    else:
        for key in sorted(occurs, key=lambda k: (-occurs[k], k)):
            if (occurs[key] > 0):
                print("{}: {}".format(key, occurs[key]))
        return
