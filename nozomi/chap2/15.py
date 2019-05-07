# -*- coding: utf-8 -*-    

print('自然数Nを入力')
n = int(input('>> '))

with open('hightemp.txt') as f:
    ls = f.readlines()
    for l in ls[-n:]:
        print(l.replace('\n',''))
       
