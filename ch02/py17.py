import sys

fname = sys.argv[1]
x = set()

f = open(fname)
line = f.readline()

while line:
    x.add(line.split()[0])
    line = f.readline()

for y in x:
    print(y)
