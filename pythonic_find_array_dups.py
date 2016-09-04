# Objective: find if an array contains duplicates

# 1,4,5,6,6,6,7,8,9,0

array = [1,2,3]

# if hashable, we can use set()

def duplicate(arr):
	seen = set()
	for i in arr:
		if i in seen:
			return True
		seen.add(i)
	return False

print duplicate(array)
