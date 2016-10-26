"""
Given a string of numbers between 1-9, write a function that prints out the
count of consecutive numbers. For example, "1111111" would be read as "seven
ones", thus giving an output of "71". Another string like "12221" would be
result in "113211"; an empty string should return empty. Other examples to
test: "999944" -> "4924" "9999222288888888888833332222" -> "49421284342"
(notice there are 12 8's in a row)

Sidenote: this algorithm is also popular with strings of consecutive
characters. Ideally, your solution should be able to work for any string of
consecutive characters AND digits: "99992222888hhhhheeeelllloooo88833332222" ->
"4942385h4e4l4o384342"

"""

def print_consecutive(input_string):
    """function to count and print the number of consecutive digits or
    characters
    input_string: string - string to use
    """

    
    ret_str = ""
    # print len(input_string)
    if not input_string == "":
        counter = 1
        prev_char = input_string[0]
        for i in xrange(1, len(input_string)):
            # print i,
            # print input_string[i]
            if input_string[i] == prev_char:
                counter += 1
            else:
                ret_str += str(counter) + prev_char
                prev_char = input_string[i]
                counter = 1
        ret_str += str(counter) + prev_char

    print ret_str


if __name__ == "__main__":
    inpt = "hello my name is josquin"
    print_consecutive(inpt)


























"""
def look_and_say(input):
    # split input
    # result_array
    # set counter to 1
    i = 0
    counter = 0
    # num_arr = list(input)
    result = ""
    if input:
        current_char = input[0]
        # loop over num_arr
        while i < len(input):
            # if not num_arr[i] and not num_array[i+1]:
            #     break
            #     if num_arr[i] == num_arr[i+1]
            #         counter += 1
            if current_char == input[i]:
                counter += 1
            # else
            #     result_array.append(counter)
            #     result_array.append(num_array[i]
            #     counter = 1
            else:
                # print "else"
                result = result + str(counter) + str(current_char)
                current_char = input[i]
                counter = 1
            i += 1
        result = result + str(counter) + str(current_char)
    else:
        result = ""
    return result

print look_and_say("22233333")
"""