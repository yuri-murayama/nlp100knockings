import random
print('文字列入力')
str = input()
strlist = str.split(' ')
for i in range(len(strlist)):
    if len(strlist[i]) > 4:
        s = strlist[i]
        s = list(s)
        ss = s.pop(0)
        ss = s.pop(len(s)-1)
        print(ss)
        random.sample(ss,len(ss))
        print(s[0]+str(ss)+s[len(s)],end = ' ')
    else:
        print(strlist[i])
print()
