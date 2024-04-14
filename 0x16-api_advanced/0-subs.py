#!/usr/bin/python3
"""Queries the Reddit API and
returns the number of subscribers
If an invalid subreddit is given,
the function should return 0.
"""
from requests import get


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers
    for a given subreddit.
    """
    # Set the Default URL strings
    base_url = 'https://www.reddit.com'
    api_uri = '{}/r/{}/about.json'.format(base=base_url, subreddit=subreddit)

    # Set an User-Agent
    user_agent = {'User-Agent': 'Python/requests'}

    # Get the Response of the Reddit API
    res = get(api_uri, headers=user_agent,
                       allow_redirects=False)
    
    # Checks if the subreddit is invalid
    if res.status_code in [302, 404]:
        return 0

    # Returns the total subscribers of the subreddit
    data = res.json()
    subscribers = data['data']['subscribers']
    return subscribers
