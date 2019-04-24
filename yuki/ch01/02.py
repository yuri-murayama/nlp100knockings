str1, str2 = list(input().split())
for i in range(len(str1)):
    if i != len(str1)-1:
        print(str1[i]+str2[i], end="")
    else:
        print(str1[i]+str2[i])
