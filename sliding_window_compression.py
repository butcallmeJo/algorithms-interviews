#!/usr/bin/env python

"""
Program to compress a string using a sliding window compression algorithm

-Consider characters one by one. Let the current character index be i.
-Take the last width characters before the current one (i.e. s[i - width, i - 1
, where s[i, j] means the substring of s from index i to index j, both
inclusive), and call it the window.
-Find such startIndex and length that s[i, i + length - 1] = s[startIndex,
startIndex + length - 1] and s[startIndex, startIndex + length - 1] is
contained within the window. If there are several such pairs, choose the one
with the largest length. If there still remains more than one option, choose
the one with the smallest startIndex.
-If the search was successful, append "(startIndex,length)" to the result and
move to the index i + length.
-Otherwise, append the current character to the result and move on to the next
one.
"""

import sys

def lossless_data_compression(input_string, width):
    """applies the compression to input_string
    input_string: string - input string to be compressed
    width: int - max width of the sliding window
    """

    # easy to read format for reading input string and width
    print "====================================================="
    print "input_string:\t\t", input_string
    print "width:\t\t\t", width

    str_len = len(input_string)
    # initializing i for index of input_string
    i = 0
    # initializing result as an empty string
    result = ""

    # to do: find a way to do the next loop more pythonic
    while i < str_len:
        # calling get_window function to get the correct window
        window = get_window(i, width)
        len_window = len(window)
        # if window not empty, then str_window created for future ease of use
        # adds the first char of input_string as the first char of result
        if len_window > 0:
            str_window = input_string[window[0]:window[-1]+1]
        else:
            str_window = ""
            # adding the first char everytime
            result += input_string[i]

        # loop to get the max length where a match in window can be found in
        # input_string. The loop goes thru the biggest length until 1
        for length in range(1, len_window+1)[::-1]:
            # if statement to make sure that current index + length does not
            # exceed the end of the input_string
            if not i+length > str_len:
                # appends the current char to result if it can't be found
                # in window
                if input_string[i] not in str_window:
                    result += input_string[i]
                    break # needed to break out of loop and move i forward

                # calls to_append and puts the return in a str var
                ret_result = to_append(input_string, i, window, length)

                if ret_result != "":
                    # moving i forward by length since ret_result contains dup
                    # char
                    result += ret_result
                    i += length-1
                    break # needed to break out of loop and move i forward
                elif length <= 1:
                    result += input_string[i]
                    break # needed to break out of loop and move i forward
        i += 1
    # formatting the result
    print "compressed string:\t", result
    print "====================================================="


def to_append(input_string, i, window, length):
    """function to return a string to append to final result
    input_string: str - full string to be compressed
    i: int - current index of the input string
    window: list - current window containing the indices of input_string
    length: int - current length to look AttributeError

    return: the result as a string. Empty string if no match was found.
    As a representation of matched string from 'start_index' and 'length'
    long.
    """

    result = ""
    for start_index in window:
        if start_index + length - 1 < i: # verified
            str_before = input_string[start_index:start_index+length] # v
            str_after = input_string[i:i+length] # verified
            if str_before in str_after:
                result = "(" + str(start_index) + "," + str(length) + ")"
                break
    return result

def get_window(index, width):
    """function to return the current window
    index: int - current index of the input string
    width: int - decides how big the window is

    <<  Take the last width characters before the current one..
        and call it the window
        >>

    return: the window as a list of indices of the original
    input string.
    """
    window = []

    # loop to insert the correct index at the beginning of the window
    # it gets all 'width' (how many) correct indices before index
    for i in range(0, index)[::-1][0:width]:
        window.insert(0, i)
    return window

if __name__ == "__main__":

    if len(sys.argv) == 3:
        INPT_STR = str(sys.argv[1])
        WIDTH = int(sys.argv[2])
    else:
        # change below or add more to test with other strings
        INPT_STR = "abacabadabacaba"
        WIDTH = 7
    lossless_data_compression(INPT_STR, WIDTH)
