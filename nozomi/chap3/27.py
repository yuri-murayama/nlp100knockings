# -*- coding: utf-8 -*-                                                                                                                                 
import re

with open('uk_kiso.txt','r') as f,open('field.txt','w') as f1,open('atai.txt','w') as f2:
    ls = f.readlines()
    for l in ls:
        #m0 =re.sub(r'(\[\[)(.*)\|','',l)
        m1 =re.sub(r'(\'\'\')|(\'\'\')','',l)
        #m0 =re.sub(r'(\[\[)(.*)\|(.*)\)','',m1)
        m0 =re.sub(r'(\[\[)(.+)\|','',m1)
        m2 =re.sub(r'(\[\[)|(\]\])','',m0)
        #m3 =re.sub(r'(.+)\|','',m2)
        m = re.match(r'^\|(.+?)(=+)(.+)$',m2)
        if m != None:
            f1.write(m.group(1).strip()+'\n')
            f2.write(m.group(3).strip()+'\n')

with open('field.txt','r') as f1,open('atai.txt','r') as f2:
    l1 = f1.read().split('\n')
    l2 = f2.read().split('\n')
    d = dict(zip(l1,l2))
    d.pop('')
    #print(d)
    for k, v in d.items():
        print('{0}:{1}'.format(k,v))
