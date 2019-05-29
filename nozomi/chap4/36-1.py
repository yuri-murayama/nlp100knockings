# -*- coding: utf-8 -*-                                                        

import collections

with open('neko.txt.mecab','r') as f:
    ls = f.readlines()
    #print(ls)                                                          
lst=[]
for l in ls:
    p = l.split('\t')
    if len(p)>=2:
        p0 = p[1].split(',')
        lst.append(
            { 'surface':p[0],
              'pos':p0[0],
              'pos1':p0[1],
              'base':p0[6]})
#print(lst[:20:]) 

lst2 = []
for lsls in lst:
    lst2.append(lsls.get('surface'))

col = collections.Counter(lst2)
col2 = col.most_common()
print(col2) 
