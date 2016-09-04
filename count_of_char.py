# How to count occurrence of a given character in a String

string_input = "hello my name is josquin gaillard and i am a student at holberton school"
character_to_find = "h"

def count_char(s, c):
    ctr = 0
    for character in s:
        if character == c:
            ctr += 1
    return ctr

print count_char(string_input, character_to_find)