# -*- coding: utf-8 -*-    

print('自然数Nを入力')
n = int(input('>> '))

with open('hightemp.txt') as f,open('a.txt','w') as f1:
    ls = f.readlines()
    st = len(ls)
    x = ls.split('\n',n)
    f1.write(x)
