# Objective: find if an array contains duplicates

arr = [1,2,3,1,4,5,6,6,6,7,8,9,0]

arr_hash = {}

for i in arr:
	if i in arr_hash:
		arr_hash[i] += 1
		print "duplicate found at index: " + str(i)
	else:
		arr_hash[i] = 1

print arr_hash
