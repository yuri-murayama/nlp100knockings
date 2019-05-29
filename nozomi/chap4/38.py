# -*- coding: utf-8 -*-                                                        
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

#plt.title('単語の出現頻度のヒストグラム')
#plt.xlabel('出現頻度をとる単語の種類数')
#plt.ylabel('出現頻度')
plt.hist(l2,range(10,200));
plt.show()
