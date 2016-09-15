import sys, os

if len(sys.argv) != 4:
    print "not enough args"
    exit()

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]

f1o = open(file1)
