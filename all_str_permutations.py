# Print all permutation of String both iterative and Recursive way?
# ask if doubles are fine

string = "abc"

def permute(string):
	str_arr = list(string)
	array = []
	for i in range(len(str_arr)+1):
		array.append(i)
	print array
	i = 1
	counter = 1
	while i < len(str_arr):
		array[i] -= 1
		j = i % 2 * array[i]
		tmp = str_arr[j]
		str_arr[j] = str_arr[i]
		str_arr[i] = tmp
		counter += 1
		print str_arr
		i = 1
		while not array[i]:
			array[i] = i
			i += 1
	print counter
permute(string)

'''using python std lib'''
import itertools

strr = itertools.permutations(string)
counter = 0
for char in strr:
	print char
	counter += 1
# print counter
