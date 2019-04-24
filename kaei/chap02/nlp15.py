#-*- coding: utf-8 -*-                                                                                                                 

filepath = "./hightemp.txt"

N = int(input())

with open(filepath) as f:
    lines = f.readlines()

for i in range(N,0,-1):
    print(lines[-i], end="")
