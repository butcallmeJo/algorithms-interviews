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

def losslessDataCompression(input_string, width):
    """applies the compression to input_string
    input_string: string - input string to be compressed
    width: int - max width of the sliding window
    """

    print "================================="
    print "input_string: ", input_string
    print "width:", width
    print "================================="

    str_len = len(input_string)
    i = 0
    result = ""

    while i < str_len:
        print "\ni:", i
        # corr_width = min(i, width)
        window = get_window(i, input_string, width)
        print "window:", window
        len_window = len(window)
        if len_window > 0:
            str_window = input_string[window[0]:window[-1]+1]
        else:
            str_window = ""
            result += input_string[i]
            print "added:", input_string[i]
        # print str_window
        print "str_window:", str_window
        # print len_window


        for length in range(1, len_window+1)[::-1]:
            if not i+length > str_len:
                print "length:", length
                if input_string[i] not in str_window:
                    result += input_string[i]
                    print "added:", input_string[i]
                    break
                # result += input_string[i]
                ret_result = return_result_to_append(input_string, i, window, length)

                if ret_result != "":
                    result += ret_result
                    print "added:", ret_result
                    i += length-1
                    break
                elif length <= 1:
                    result += input_string[i]
                    print "added:", input_string[i]
                    break

        # print "(" + str(start_index) + "," + str(length) + ")",
        i += 1
    print result

def return_result_to_append(input_string, i, window, length):
    """returns what to append to result"""

    result = ""
    for start_index in window:
        if start_index + length - 1 < i: # verified
            str_before = input_string[start_index:start_index+length] # v
            str_after = input_string[i:i+length] # verified
            print "str_before:", str_before
            print "str_after:", str_after
            if str_before in str_after:
                # print "yes"
                # print input_string[start_index:start_index+length-1]
                # print input_string[i]
                result = "(" + str(start_index) + "," + str(length) + ")"
                break
    return result

def get_window(index, input_string, width):
    window = []

    for i in range(0, index)[::-1][0:width]:
        # print str(i) + input_string[i]
        window.insert(0, i)
    return window

if __name__ == "__main__":
    INPT_STR = "abacabadabacaba"
    WIDTH = 7
    losslessDataCompression(INPT_STR, WIDTH)
    INPT_STR = "abracadabra"
    WIDTH = 5
    losslessDataCompression(INPT_STR, WIDTH)
    INPT_STR = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    WIDTH = 12
    losslessDataCompression(INPT_STR, WIDTH)
