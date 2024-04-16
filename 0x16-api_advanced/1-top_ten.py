#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
for a given subreddit"""

import requests


def top_ten(subreddit):
    """function that queries the Reddit API and returns the number of
    subscribers for a given subreddit"""
    url = f'https://oauth.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    CLIENT_ID = 'VJEVTB5HwkOSJq8wSdrucg'
    SECRET_KEY = 'JA0DqIER3KiHc39Oy19cJ43DRsJOTw'
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    data = {
        'grant_type': 'password',
        'username': 'tarikmath512',
        'password': 'vKC?!*e68YHF7E!'
    }
    res_post = requests.post('https://www.reddit.com/api/v1/access_token',
                             auth=auth, data=data, headers=headers)
    TOKEN = res_post.json()['access_token']
    headers['Authorization'] = f'Bearer {TOKEN}'
    res1 = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        res_data = response.json()
        for i in range(10):
            post = res_data.get('data').get('children')[i]
            print(post.get('data').get('title'))
    else:
        return None
