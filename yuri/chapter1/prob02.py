s1 = 'パトカー'
s2 = 'タクシー'

lst = []
for c1, c2 in zip(s1, s2):
    lst.append(c1)
    lst.append(c2)
print(''.join(lst))
