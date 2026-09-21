#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'


def retrieve_events(url):
    """Download event data from a GitHub events URL and return it as a Python object.

    Fetches the JSON text at `url` and converts it with json.loads(). On success
    the result is a list of dictionaries, one per event.
    """
    json_text = requests.get(url).text
    events = json.loads(json_text)
    return events


def print_events(events, n=5):
    """Print the first n events as 'type :: repo' lines.

    Each event is a dictionary from the GitHub events API. The line shows the
    event's 'type' field and the repository name from its nested 'repo' field.
    """
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)


def main():
    """Print the GitHub user and URL, then fetch and print recent events.

    Uses the module-level GHUSER and url, downloads the user's events with
    retrieve_events(), and prints the first five with print_events().
    """
    print(GHUSER)
    print(url)
    events = retrieve_events(url)
    print_events(events)


if __name__ == "__main__":
    main()
