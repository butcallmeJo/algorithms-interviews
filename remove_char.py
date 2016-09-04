# Objective: remove any given character from a string

str_input = "hello"
ommit_char = "o"

def rm_char(str_input, ommit_char):
	ret_str = ""
	for char in str_input:
		if char != ommit_char:
			ret_str = ret_str + char
	return ret_str

print rm_char(str_input, ommit_char)
