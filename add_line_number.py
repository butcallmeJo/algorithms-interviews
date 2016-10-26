#!/usr/bin/env python

"""
Given a random multi-line program written in any language, write another
program that will print out the first program with line numbers printed out
before each line of the program. Format it so the program's indentation isn't
affected by the new line numbers (ie - account for the fact that the added line
numbers will take up different amounts of space depending on how many digits
there are in the number).
"""

import os
import sys

def add_line_number(filename):
    """function to add line number at the beginning of a line
    of a given program"""
    temp = "temp_" + filename
    counter = 1
    with open(filename, 'r') as f:
        with open(temp, 'w') as f2:
            for line in f.readlines():
                f2.write(str(counter) + ": " + line)
                counter += 1
    os.rename(temp, filename)

if __name__ == "__main__":
    # Check if arg/file is given:
    if not len(sys.argv) == 2:
        print "please provide only one file"
        exit()
    else:
        add_line_number(sys.argv[1])
