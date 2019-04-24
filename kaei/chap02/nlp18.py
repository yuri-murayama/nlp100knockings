#-*- coding: utf-8 -*-
import numpy as np

filepath = "./hightemp.txt"

lst = []
with open(filepath) as f:
    lines = f.readlines()
    for line in lines:
        line = line.split("\t")
        lst.append(line[2])

index = np.argsort(lst)[::-1]

for i in index:
    print(lines[i], end="")
