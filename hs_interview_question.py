# def say_hello():
#     print 'Hello, World'

# for i in xrange(5):
#     say_hello()


#
# Your previous Plain Text content is preserved below:
#
# This is just a simple shared plaintext pad, with no execution capabilities.
#
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
#
# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/profile
#
# Enjoy your interview!
#
#
# // Given a string of numbers between 1-9, write a function that prints out the count of consecutive numbers.
# // For example, "1111111" would be read as "seven ones", thus giving an output of "71". Another string like "12221" would be result in "113211".
# // "" -> ""



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

print look_and_say("99992222888hhhhheeeelllloooo88833332222")
