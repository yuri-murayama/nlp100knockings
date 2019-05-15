# -*- coding: utf-8 -*-    

import json 

with open('jawiki-country.json','r') as f,open('uk.txt','w') as f1:
    for l in f:
        t = json.loads(l)
        #print(t)
        if t['title']=='イギリス':
            t2 = t['text']
            #print(t2)
            f1.write(t2)
        
        
