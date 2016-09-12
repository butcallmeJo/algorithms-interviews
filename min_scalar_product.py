# given 2 vectors: v1(x1, x2, x3,...,xN) and v2(y1, y2, y3,...,yN)
# choose 2 permutations of coordinates of v1 and v2 so that the scalar product is the smallest possible
# give that product

# input format:
# T (test cases)
# N (number of coordinates for each test cases)
# x1 x2 x3 ... xN (vector v1)
# y1 y2 y3 ... yN (vector v2)

# output expected:
# Case #X: Y (X is the test case number, Y is the min scalar product)

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    v1 = [int(i) for i in sys.stdin.readline().split()]
    v2 = [int(i) for i in sys.stdin.readline().split()]
    # Can refactor and make code better:
    if len(v1) > 1:
        v1_biggest_num = v1[0]
        v1_biggest_num_2 = v1[1]
        v1_smallest_num = v1[0]
        v1_smallest_num_2 = v1[0]
        if v1[1] > v1_biggest_num:
            v1_biggest_num = v1[1]
            v1_biggest_num_2 = v1[0]
        if v1[1] < v1_smallest_num:
            v1_smallest_num = v1[1]
            v1_smallest_num_2 = v1[0]
    if len(v2) > 1:
        v2_biggest_num = v2[0]
        v2_biggest_num_2 = v2[1]
        v2_smallest_num = v2[0]
        v2_smallest_num_2 = v2[0]
        if v2[1] > v2_biggest_num:
            v2_biggest_num = v2[1]
            v2_biggest_num_2 = v2[0]
        if v2[1] < v2_smallest_num:
            v2_smallest_num = v2[1]
            v2_smallest_num_2 = v2[0]

    for i in v1:
        if i > v1_biggest_num:
            v1_biggest_num = i
        elif i > v1_biggest_num_2:
            v1_biggest_num_2 = i
        elif i < v1_smallest_num:
            v1_smallest_num = i
        elif i < v1_smallest_num_2:
            v1_smallest_num_2 = i

    for i in v2:
        if i > v2_biggest_num:
            v2_biggest_num = i
        elif i > v2_biggest_num_2:
            v2_biggest_num_2 = i
        elif i < v2_smallest_num:
            v2_smallest_num = i
        elif i < v2_smallest_num_2:
            v2_smallest_num_2 = i

    print v1_biggest_num, v1_biggest_num_2, v1_smallest_num, v1_smallest_num_2
    print v2_biggest_num, v2_biggest_num_2, v2_smallest_num, v2_smallest_num_2

'''
test inputs:

1:
2\n3\n1 3 -5\n-2 4 1\n5\n1 2 3 4 5\n1 0 1 0 1

2
3
1 3 -5
-2 4 1
5
1 2 3 4 5
1 0 1 0 1

'''