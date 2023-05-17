#!/usr/bin/python3
'''contains a function that queries the Reddit API
Usage:
   ./2-recurse.py
Author:
    Abdulsalam Abdulsomad .A. - May 17th, 2023.
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''A recursive function that queries the Reddit API and return
s a list containing the titles of all hot articles for a given subreddit
         parameters:
        ***********
            subreddit(str): subreddit to query.
            hot_list(list): list of all hot articles
            after(str): aids pagination(next page)
        Return:
        *******
            Returns all hot articles.
        Raise:
        ******
             void
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'User-Agent': 'MyBot/1.0'}
    # set the value of after and page limit
    params = {'after': after, 'limit': 100} if after else {'limit': 100}
    # query the API
    response = requests.get(url,
                            headers=header,
                            params=params,
                            allow_redirects=False)
    # if there was an error(invalid subreddit) return None
    if response.status_code != 200:
        return (None)
    # otherwise:
    else:
        # get json representation of the response
        data = response.json()
        # get all hot posts
        hots = data['data']
        posts = 'children'
        # test if there is any hot article
        if posts in hots:
            # loop through all hot posts and append them to hot_list
            for post in hots[posts]:
                hot_list.append(post['data']['title'])
            # get the new value of after
            after = hots['after']
            # if after is not None call the function recursively
            if after:
                return (recurse(subreddit, hot_list, after))
            # otherwise return hot_list
            else:
                return (hot_list)
        # otherwise return None if there is no article
        else:
            return (None)
