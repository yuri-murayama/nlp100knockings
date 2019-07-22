import sys

f = open(sys.argv[1])
lines = f.readlines()
print(len(lines))

f.close()
