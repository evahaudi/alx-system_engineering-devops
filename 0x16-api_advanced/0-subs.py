#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            subscribers = data.get("subscribers", 0)
            return subscribers
        else:
            print("Invalid subreddit or unable to fetch data.")
            return 0
    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0

