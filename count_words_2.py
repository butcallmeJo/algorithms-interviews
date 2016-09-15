import sys

if len(sys.argv) != 2:
    print "Not correct number of args"
    exit(1)

f = open(sys.argv[1])
# f.read()
wc = {}
for word in f.read().split():
    if word not in wc:
        wc[word] = 1
    else:
        wc[word] += 1

print wc

f.close()