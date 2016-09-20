#!/usr/bin/env python

import requests
import sys
import argparse
import datetime
# uncomment next line if making more than 60 requests per hour
# import config from github_config

"""all_github_repos.py

Python script to get all Github repositories from a given username and order
them by creation date as well as output their last commits' SHA1.
"""

def fetch_all_repositories(user):
    """function to fetch_all_repositories from user and process the data
    user - the username used to construct the correct requests to the Github
    API.
    """
    resp_repos = requests.get('https://api.github.com/users/' + user + '/repos')
    repos_json = resp_repos.json()
    repos_dict = {}
    for i in range(len(repos_json)):
        name = repos_json[i]["name"]
        date = datetime.datetime.strptime(
            repos_json[i]["created_at"], '%Y-%m-%dT%H:%M:%SZ'
            )
        sha = requests.get('https://api.github.com/repos/' + user + '/' + name + '/commits').json()[0]["sha"]
        if name not in repos_dict:
            repos_dict[name] = [date, sha]
    
    print repos_dict

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