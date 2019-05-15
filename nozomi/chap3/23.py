# -*- coding: utf-8 -*-    

import re
import json

with open('uk.txt','r') as f:
    ls = f.readlines()
    for l in ls:
        m = re.match(r'^(=+)(.+?)(=+)$',l)
        if m != None:
            print(m.group(2))
            print('レベル：'+str(len(m.group(1))-1))
        
