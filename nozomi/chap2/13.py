# -*- coding: utf-8 -*-    

with open('col.txt','w') as f,open('col1.txt') as f1,open('col2.txt') as f2:
    for (l1,l2) in zip(f1,f2):
        f.write(l1.strip()+'\t'+l2.strip()+'\n')


