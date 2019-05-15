# -*- coding: utf-8 -*-    

with open('uk.txt','r') as f,open('uk_ctg.txt','w') as f1:
    ls = f.readlines()
    for l in ls:
        if 'Category' in l:
            print(l.strip())
            f1.write(l.strip()+'\n')


