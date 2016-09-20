#!/usr/bin/env python

import requests
import sys
import argparse
import config from github_config

"""all_github_repos.py

Python script to get all Github repositories from a given username and order
them by creation date as well as output their last commits' SHA1.
"""

def fetch_all_repositories(user):
    """function to fetch_all_repositories from user and process the data
    user - the username used to construct the correct requests to the Github
    API.
    """
    resp = requests.get('')

def main(argv):
    """Main part of the program"""

    # Parsing with argparse for the github username
    parser = argparse.ArgumentParser(
        description="Get all Github repositories from a given Github username"
    )
    parser.add_argument(
        "--username", "-u", dest="username", metavar='USERNAME',
        type=str, required=True,
        help=(
            "The Github username needed."
        )
    )
    args = parser.parse_args(argv[1:])
    user = args.username
    fetch_all_repositories(user)

if __name__ == "__main__":
    try:
        main(sys.argv)
    except:
        sys.exit()