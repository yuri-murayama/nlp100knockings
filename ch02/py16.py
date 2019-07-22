import sys
import math

f = open(sys.argv[1])
lines = f.readlines()

n = int(sys.argv[2])

count = len(lines)
unit = math.ceil(count / n)

for i in range(unit):
    w = open("nsplit%s.txt" % str(i), "w")
    w.writelines(lines[unit * i: unit * (i + 1)])
