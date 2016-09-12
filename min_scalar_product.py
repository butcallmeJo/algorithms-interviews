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
    if len(v1) > 1:
        biggest_num = v1[0]
        biggest_num_2 = v1[1]
    if v1[1] > biggest_num:
        biggest_num = v1[1]
        biggest_num_2 = v1[0]
    if len(v2) > 1:
        biggest_num = v2[0]
        biggest_num_2 = v2[1]
    if v2[1] > biggest_num:
        biggest_num = v2[1]
        biggest_num_2 = v2[0]

    for i in v1:
        if i > biggest_num:
            biggest_num = i
        elif i > biggest_num_2:
            biggest_num_2 = i
        