# -*- coding: utf-8 -*-    

with open('hightemp.txt') as f:
    l = f.readlines()
    l.sort(key=lambda i: float(i.split('\t')[2]),reverse=True)

for i in l: 
    ni = i.strip()
    print(ni)
