# How to find first non repeated character of a given String

string_input = "hello my name is Josquin Gaillard and I am a studenty at Holberton ScHool"

def find_non_repeat_char(s):
    char_hash = {}
    for c in s:
        if c in char_hash:
            char_hash[c] += 1
        else:
            char_hash[c] = 1
    for c in s:
        if char_hash[c] == 1:
            return c

print find_non_repeat_char(string_input)