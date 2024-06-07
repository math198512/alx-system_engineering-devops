#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
for a given subreddit"""

import requests, requests.auth


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    username = "tarikmath512"
    password = "8ig8W7Z$e$Zev*z"
    CLIENT_ID = "VJEVTB5HwkOSJq8wSdrucg"
    CLIENT_SECRET = "JA0DqIER3KiHc39Oy19cJ43DRsJOTw"
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "password", "username": username, "password": password}
    TOKEN_ACCESS_ENDPOINT = "https://www.reddit.com/api/v1/access_token"
    
    headers = {"User-Agent": "Mozilla/5.0"}
    auth_response = requests.post(TOKEN_ACCESS_ENDPOINT, data=post_data, headers=headers, auth=client_auth)
    TOKEN = auth_response.json()['access_token']
    headers['Authorization'] = f'bearer {TOKEN}'
    url = "https://oauth.reddit.com/r/{}/about/".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return response.status_code 