# -*- coding: utf-8 -*-    

import re
import json

with open('uk.txt','r') as f:
    ls = f.readlines()
    for l in ls:
        m = re.match(r'^(\[\[)?(ファイル|File):(.*)(\]\])?$',l)
        if m != None:
            #print(m.group(0))
            m1 = m.group(0)
            m2 = m1.split('|')[0]
            m3 = m2.split(':')[1]
            print(m3)
    
        
