# -*- coding: utf-8 -*-    

import re

with open('uk_ctg.txt','r') as f:
    ls = f.readlines()
    for l in ls:
        m = re.match(r'^\[\[Category:(.*)\]\]$',l)
        m1 = m.group(1)
        m2 = m1.split('|')[0]
        print(m2)
