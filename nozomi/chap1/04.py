# -*- coding: utf-8 -*- 

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

s = s.replace('.','')
s = s.replace(',','')
s = s.split(' ')

l = [0,4,5,6,7,8,14,15,18]
d = dict()

for w in range(0,len(s)):
    if w in l: 
       d[s[w][0]]=w+1
    else:
        d[s[w][0:2]]=w+1

print(d)
