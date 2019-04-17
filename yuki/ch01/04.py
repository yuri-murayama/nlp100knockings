str = input()
d = {}
strlist = str.split(" ")
l = [1,5,6,7,8,9,15,16,19]
for i in range(len(strlist)):
    str = strlist[i]
    if i+1 in l:
        d[str[0:1]] = i+1
    else:
        d[str[0:2]] = i+1
print(d)
    
