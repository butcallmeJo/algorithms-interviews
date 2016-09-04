# Objective: get all string permutations recursively
# need to recode this later or find another way to code this

string_input = "abcd"

def permute_recurse(str_input):
    if len(str_input) <= 1:
        return [str_input]
    prev_list = permute_recurse(str_input[1:len(str_input)])
    # print prev_list
    next_list = []
    # print "test"
    for i in range(len(prev_list)):
        for j in range(len(str_input)):
            new_string = prev_list[i][:j] + str_input[0] + prev_list[i][j:len(str_input)-1]
            if new_string not in next_list:
                next_list.append(new_string)
    return next_list
        
        
print '\n'.join(permute_recurse(string_input))
