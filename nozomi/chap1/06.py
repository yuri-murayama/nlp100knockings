# -*- coding: utf-8 -*-   

s1 = "paraparaparadise"
s2 = "paragraph"

s1 = s1.replace('.','')
s1 = s1.replace(',','')
s1 = s1.replace(' ','')
print('X')
for w1 in range(0,len(s1)-1):
    print(s1[w1],end='')
    print(s1[w1+1])
s2 = s2.replace('.','')
s2 = s2.replace(',','')
s2 = s2.replace(' ','')
print()
print('Y')
for w2 in range(0,len(s2)-1):
    print(s2[w2],end='')
    print(s2[w2+1])

print()

print("XとYの和集合")

l=[]

for w1 in range(0,len(s1)-1):
    for w2 in range(0,len(s2)-1):
        if not s1[w1]==s2[w2] or s1[w1+1]==s2[w2+1]:
            l.append(s1[w1]+s1[w1+1])
            l.append(s2[w2]+s2[w2+1])

print(set(l))




print()

print("XとYの積集合")

l=[]

for w1 in range(0,len(s1)-1):
    for w2 in range(0,len(s2)-1):
        if s1[w1]==s2[w2] and s1[w1+1]==s2[w2+1]:
            l.append(s1[w1]+s1[w1+1])
            
print(set(l))


print()

print("XとYの差集合")

l=[]

for w1 in range(0,len(s1)-1):
    for w2 in range(0,len(s2)-1):
        if  s1[w1]!=s2[w2] and s1[w1+1]!=s2[w2+1]:
            l.append(s1[w1]+s1[w1+1])

print(set(l))
