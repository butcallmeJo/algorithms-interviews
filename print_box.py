#!/usr/bin/env python

"""print_box.python
script to take a number 'n' from cmd line input and print a square
of n size.
"""

import sys

def print_box(n):
    """print_box function
    n: int - size of box
    """
    if n > 80:
        print "error, please input a correct integer from 0 to 80"
        print "n out of range"
        sys.exit(1)
    for i in xrange(n):
        for j in xrange(n):
            if (i == 0 and j == 0) or (i == n-1 and j == 0):
                print "o",
            elif (i == 0 and j == n-1) or (i == j and j == n-1):
                print "o"
            elif i == 0 or i == n-1:
                print "-",
            elif j == 0:
                print "|",
            elif j == n-1:
                print "|"
            else:
                print " ",

if __name__ == "__main__":
    try:
        print_box(int(sys.argv[1]))
    except (ValueError, IndexError) as e:
        print "error, please input a correct integer from 0 to 80"
        print e
        sys.exit(1)
