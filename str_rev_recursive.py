# Objective: reverse a string using recursion

string = "hello"

# reversing a str recursively means you swap the 2 extremes and then you go in
def str_rev_recurse(string):
	if len(string)<=1:
		return string
	else:
		# puts the first letter at the end and recursively goes thru string without the first letter
		return str_rev_recurse(string[1:]) + string[0]

print string
print str_rev_recurse(string)

# learned something new in python
