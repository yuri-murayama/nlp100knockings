# -*- coding: utf-8 -*-    

print('自然数Nを入力')
n = int(input('>> '))

with open('hightemp.txt') as f:
    for x,l in enumerate(f):
        if x<n:
            print(l.replace('\n',''))
        else:
            break
