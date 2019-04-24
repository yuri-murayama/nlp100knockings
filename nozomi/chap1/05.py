# -*- coding: utf-8 -*-  

s = "I am an NLPer"

s = s.replace('.','')
s = s.replace(',','')
s = s.split(' ')

for w in range(0, len(s)-1):
    print(s[w],end=" ")
    print(s[w+1])

print()

s1 = "I am an NLPer"
s1 = s1.replace('.','')
s1 = s1.replace(',','')
s1 = s1.replace(' ','')
for w1 in range(0,len(s1)-1):
    print(s1[w1],end='')
    print(s1[w1+1])
