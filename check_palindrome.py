import timeit
# check if a string is a palindrome

# pythonic way (with methods)

str_input = "abbba"

def is_palindrome(str_input):
	if str_input == str_input[::-1]:
		return True
	return False
print timeit.timeit("'abbba' == 'abbba'[::-1]", number=10000)
print "func 1: " + str(is_palindrome(str_input))

# unpythonic way (more like C)

def is_palindrome2(str_input):
	for i in range(len(str_input)/2):
		if str_input[i] != str_input[len(str_input)-i-1]:
			return False
	return True

print timeit.timeit("for i in range(len('abbba')/2): 'abbba'[i] != 'abbba'[len('abbba')-i-1]", number=10000)
print "func 2: " + str(is_palindrome2(str_input))
