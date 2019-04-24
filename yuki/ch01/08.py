str = input()
for i in range(len(str)):
    if 97 <= ord(str[i]) and ord(str[i]) <=122:
        print(chr(219-ord(str[i])),end='')
    else:
        print(str[i])
print()
