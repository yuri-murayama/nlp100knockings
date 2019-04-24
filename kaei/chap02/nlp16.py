#-*- coding: utf-8 -*-                                                                                                                 
import numpy as np

filepath = "./hightemp.txt"

N = int(input())

with open(filepath) as f:
    lines = f.readlines()

lst = list(np.array_split(lines, N))

for i, l in enumerate(lst):
    with open("output%d.txt" %i, mode='w') as f:
        f.writelines(l)
