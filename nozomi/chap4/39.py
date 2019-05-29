# -*- coding: utf-8 -*-   
import numpy as np                                                     
import matplotlib.pyplot as plt
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
#print(col2[:20:]) 

l1 = []
l2 = []
for col0 in col2:
    l1.append(col0[0])
    l2.append(col0[1])
#print(l1[:10:])


rnk = list(range(1,len(l2)+1))
fig,ax = plt.subplots()
ax.plot(l2, rnk)
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
