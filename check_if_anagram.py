#  How to check if two String are Anagram

string1 = "myisjalalalalalalhelloname"
string2 = "lalalalalalahellomynameis"

def check_if_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    str_char_hash = {}
    for c1 in str1:
        if c1 in str_char_hash:
            str_char_hash[c1] += 1
        else:
            str_char_hash[c1] = 1
    for c2 in str2:
        if c2 in str_char_hash:
            str_char_hash[c2] -= 1
        else:
            return False
    for key in str_char_hash:
        if str_char_hash[key] != 0:
            return False
        else:
            return True

print check_if_anagram(string1, string2)
