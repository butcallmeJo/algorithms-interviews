#!/usr/bin/env python

import requests
import sys
import argparse
import datetime

"""all_github_repos.py

Python script to get all Github repositories from a given username and order
them by creation date as well as output their last commits' SHA1.
"""

def sort_dict_by_date(repos_dict):
    sorted_list = sorted(repos_dict.items(), key=lambda e: e[1][0])
    sorted_list = [x[0] for x in sorted_list]
    return sorted_list

def fetch_all_repositories(user):
    """function to fetch_all_repositories from user and process the data
    user - the username used to construct the correct requests to the Github
    API.
    """
    resp_repos = requests.get(
        'https://api.github.com/users/' + user + '/repos',
        auth=('Holberton_School', 'fffa38b10948aa7eff293682308672bc95672ae3')
        )
    repos_json = resp_repos.json()
    repos_dict = {}
    for i in range(len(repos_json)):
        name = repos_json[i]["name"]
        date = datetime.datetime.strptime(
            repos_json[i]["created_at"], '%Y-%m-%dT%H:%M:%SZ'
            )
        try:
            sha = requests.get('https://api.github.com/repos/' + user + '/' + name + '/commits', auth=('Holberton_School', 'fffa38b10948aa7eff293682308672bc95672ae3')).json()[0]["sha"]
        except:
            print "error getting sha for %s" % (name)
        if name not in repos_dict:
            repos_dict[name] = [date, sha]
    
    sorted_list = sort_dict_by_date(repos_dict)
    
    for repo in sorted_list:
        print repo
        print "\t%s" % (str(repos_dict[repo][0]))
        print "\t%s\n" % (repos_dict[repo][1])

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
    main(sys.argv)
