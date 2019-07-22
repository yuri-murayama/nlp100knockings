import sys

f = open(sys.argv[1])
str = f.read()
print(str.replace("\t", " "))
