# In an array 1-100 numbers are stored, one number is missing how do you find it?

max = 100
arr = [i for i in range(1, max+1)]
# print arr
num_to_delete = 58
del arr[num_to_delete-1]
# print arr

# Hash/Storage method:
def arr_to_hash_method(a, max):
    hash_of_a = {}
    for i in a:
        hash_of_a[i] = i
    for num in range(1, max+1):
        if num not in hash_of_a:
            return num
    return "couldn't find missing"

print "storing method, missing number is", arr_to_hash_method(arr, max)

# better and faster method using only one loop and math:
def quick_math_method(a, max):
    # get sum of all nums from 1 to max
    expected = 0
    for i in range(max+1):
        expected += i
    total = 0
    total = sum(a)
    missing = expected - total
    return missing

print "math method, missing number is", quick_math_method(arr, max)    