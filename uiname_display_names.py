#!usr/bin/env python
"""using uinames.com's API, display 5 female names
objective changed to get input for optional gender, optional number and
optional region.

API format: http://uinames.com/api/?amount=25?gender=female?region=germany
"""

import argparse
import requests
import sys

def get_and_display_names(number, gender, region):
    if gender and region:
        resp = requests.get(
            'http://uinames.com/api/?amount=%i?gender=%s?region=%s'
            % (number, gender, region)
        )
    elif gender:
        resp = requests.get(
            'http://uinames.com/api/?amount=%i?gender=%s'
            % (number, gender)
        )
    elif region:
        resp = requests.get(
            'http://uinames.com/api/?amount=%i?region=%s'
            % (number, region)
        )
    else:
        resp = requests.get(
            'http://uinames.com/api/?amount=%i'
            % (number)
        )
    print resp.status_code
    resp_json = resp.json()
    for i in range(len(resp_json)):
        print resp_json[i]["name"], resp_json[i]["surname"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="make a request to uinames.com's API and display names \
        in STDOUT"
    )
    parser.add_argument(
        "--number", "-n", dest="number", metavar='NUMBER',
        type=int, default=5,
        help=(
            "How many names to return. Default is 5."
        )
    )
    parser.add_argument(
        "--gender", "-g", dest="gender", metavar='GENDER',
        type=str, default=None,
        help=(
            "Specify the gender of names to return. Default is None."
        )
    )
    parser.add_argument(
        "--region", "-r", dest="region", metavar='REGION',
        type=str, default=None,
        help=(
            "Specify a region from where to get names. Default is None."
        )
    )
    args = parser.parse_args(sys.argv[1:])
    number = args.number
    gender = args.gender
    region = args.region
    get_and_display_names(number, gender, region)