#!/usr/bin/python3
'''contains a function that queries the Reddit API
Usage:
   ./0-subs.py
Author:
    Abdulsalam Abdulsomad .A. - May 16th, 2023.
'''
import requests


def top_ten(subreddit):
    '''A  function that queries the Reddit API and prints the
 titles of the first 10 hot posts listed for a given subreddit
        parameters:
        ***********
            subreddit(str): subreddit to query.
        Return:
        *******
            Prints top 10 hot posts.
        Raise:
        ******
             void
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'User-Agent': 'MyBot/1.0'}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        print("None")
    else:
        data = response.json()
        hot_10 = data['data']['children'][0:10]
        for post in hot_10:
            print(post['data']['title'])
