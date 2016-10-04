#!/usr/bin/env python

"""
Given a random multi-line program written in any language, write another program that will print out the first program with line numbers printed out before each line of the program. Format it so the program's indentation isn't affected by the new line numbers (ie - account for the fact that the added line numbers will take up different amounts of space depending on how many digits there are in the number).
"""

import os
import sys
import argparse

def add_line_number(filename, new_filename):
    """function to add line numbers to a file"""
    with open(filename, 'r') as input_f:
        with open(new_filename, 'w') as output_f:
            count = 0
            for line in input_f:
                output_f.write(str(count) + '\t' + line)
                count += 1



def main():
    parser = argparse.ArgumentParser(description="script to add line number")
    parser.add_argument(
        '--input_file', '-i', metavar='FILE', type=str,
        dest='filename', required=True,
        help=("the filename to which to add the line numbers")
        )
    parser.add_argument(
        '--new_file', '-n', metavar='FILE', type=str,
        dest='new_filename', required=True,
        help=("the filename to which to add the line numbers")
        )
    args = parser.parse_args()
    filename = args.filename
    new_filename = args.new_filename
    add_line_number(filename, new_filename)

if __name__ == "__main__":
    main()
