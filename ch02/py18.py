import sys

f = open(sys.argv[1])
lines = f.readlines()

for line in sorted(lines,key = lambda y :y.split()[2],reverse=False):
    print(line)
