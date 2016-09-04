# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

arg_list = [int(i) for i in sys.stdin.readline().split(" ")]
num = [int(i) for i in sys.stdin.readline().split(" ")]

for i in range(min(arg_list[1],arg_list[0]-1)):
    big_index = num.index(max(num[i:]))
    num[i], num[big_index] = num[big_index], num[i]

for n in num:
    print n,
