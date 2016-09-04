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
