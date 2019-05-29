# -*- coding: utf-8 -*-  

import re

with open('uk_kiso.txt','r') as f,open('field.txt','w') as f1,open('atai.txt','w') as f2:
    ls = f.readlines()
    for l in ls:
        m = re.match(r'^\|(.+?)(=+)(.+)$',l)
        if m != None:
            #print(m.group(1))
            #print(m.group(3))
            f1.write(m.group(1).strip()+'\n')
            f2.write(m.group(3).strip()+'\n')
        

with open('field.txt','r') as f1,open('atai.txt','r') as f2:
    l1 = f1.read().split('\n')
    l2 = f2.read().split('\n')
    #print(l1)
    #print(l2)
    d = dict(zip(l1,l2))
    d.pop('')
    #print(d)
    for k, v in d.items():
        print('{0}:{1}'.format(k,v))
