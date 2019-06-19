# -*- coding: utf-8 -*-

filepath = "./hightemp.txt"

lst0 = []
lst1 = []

with open(filepath) as f:
    print(f)
    lines = f.readlines()
    for line in lines:
        line = line.split("\t")
        lst0.append(line[0])
        lst1.append(line[1])

with open("./col1.txt", mode='w') as f:
    f.write('\n'.join(lst0))

with open("./col2.txt", mode='w') as f:
    f.write('\n'.join(lst1))
