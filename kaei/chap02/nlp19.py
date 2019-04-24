#-*- coding: utf-8 -*-

filepath = "./hightemp.txt"

lst = []
with open(filepath) as f:
    lines = f.readlines()
    for line in lines:
        line = line.split("\t")
        lst.append(line[0][:-1])

pref = {}

for i in lst:
    if i in pref.keys():
        pref[i] += 1
    else:
        pref[i] = 1

for k in sorted(pref.items(), key=lambda x: -x[1]):
    print(k[0])
    
