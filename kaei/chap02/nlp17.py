#-*- coding: utf-8 -*-

filepath = "./col1.txt"

with open(filepath) as f:
    lines = f.readlines()

pref = []

for line in lines:
    if line[:-1] not in pref:
        pref.append(line[:-1])

print(pref)
