# -*- coding: utf-8 -*-    

import collections

with open('hightemp.txt') as f:
   ls = f.readlines()
   # l.sort(key=lambda i: float(i.split('\t')[0],reverse=True)


with open('test.txt','w') as f:
   for l in ls: 
      k = l.split('\t')

      f.write(k[0]+'\n')

with open('test.txt') as f:
   x = f.readlines()
   y = ''.join(x)
   z = y.split('\n')
   xyz = collections.Counter(z)
   a = xyz.most_common()
   a.pop(-1)
   print(a)

