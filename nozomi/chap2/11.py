# -*- coding: utf-8 -*-   

with open('hightemp.txt','r') as f:
    txt = f.read()
    txt2 = txt.replace('\t',' ')
print(txt2)
