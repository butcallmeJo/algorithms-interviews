#  How to convert numeric String to int

string_input = "1111111"

# pythonic methods:
int_of_string = int(string_input)
print int_of_string + 1

# more C style:

def a_to_i(s):
    res = 0
    for c in s:
        res = 10*res + ord(c) - ord('0')
    return res

print a_to_i(string_input) + 1