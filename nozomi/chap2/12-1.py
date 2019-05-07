# -*- coding: utf-8 -*-   

with open('hightemp.txt') as f,open('col1.txt','w') as f1,open('col2.txt','w') as f2:
    for l in f:
        w = l.split('\t')
        f1.write(w[0]+'\n')
        f2.write(w[1]+'\n')
