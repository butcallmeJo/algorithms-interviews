#!/usr/bin/env python

import argparse

"""
Script to count the length of an integer in multiple ways.
"""

def method_1(num):
    print len(str(num))

def method_2(num):
    length = 1
    while num >= 10:
        length += 1
        num = num / 10
    print length

def main():
    parser = argparse.ArgumentParser(
        description="Script to count the length of an integer"
    )
    parser.add_argument(
        "--method", "-m", dest="method", metavar="N", type=int,
        help=(
            "method 1 is pythonic, method 2 is algorithmic"
        )
    )
    parser.add_argument(
        "--integer", "-i", dest="integer", metavar="i", type=int, required=True,
        help=(
            "input the integer here"
        )
    )
    args = parser.parse_args()
    method = args.method
    integer = args.integer
    if method == 12:
        method_1(integer)
        method_2(integer)

    elif method == 1:
        method_1(integer)
    elif method == 2:
        method_2(integer)
    else:
        print "Sorry only method 1 and 2 available for now"

if __name__ == "__main__":
    main()