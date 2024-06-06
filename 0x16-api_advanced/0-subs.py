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
    client_auth = ""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
