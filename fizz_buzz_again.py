#!/usr/bin/env python

"""fizz buzz program"""

def fizz_buzz(fizz_num, buzz_num):
    """function to print out all numbers from 1 to 100 and replacing the numbers
    completely divisible by the fizz number by 'Fizz', the numbers completely
    divisible the buzz number by 'Buzz' and the numbers completely divisible by
    both by 'FizzBuzz'
    """

    for i in range(1, 101):
        # loop to go from 1 included to 101 excluded
        if i % (fizz_num*buzz_num) == 0:
            print "FizzBuzz",
        elif i % fizz_num == 0:
            print "Fizz",
        elif i % buzz_num == 0:
            print "Buzz",
        else:
            print i,

fizz_buzz(7, 5)