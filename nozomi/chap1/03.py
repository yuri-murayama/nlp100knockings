# -*- coding: utf-8 -*-  

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

s = s.replace('.','')
s = s.replace(',','')
s = s.split(' ')

for w in s:
    print(len(w),end = "")
print()
