import sys
from collections import defaultdict

fname = sys.argv[1]
x = defaultdict(int)

f = open(fname)
line = f.readline()

while line:
    x[line.split()[0]] += 1
    line = f.readline()

for s, t in sorted(x.items(), key=lambda x: x[1], reverse=True):
    print(s)
