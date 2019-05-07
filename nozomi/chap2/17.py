# -*- coding: utf-8 -*-    

with open('hightemp.txt') as f:
    pr = set()
    for l in f:
        pr.add(l.split('\t')[0])

for i in pr:
    print(i)
