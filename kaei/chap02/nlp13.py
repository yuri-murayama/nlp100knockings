# -*- coding: utf-8 -*-

file1 = "./col1.txt"
file2 = "./col2.txt"

with open(file1) as f:
    lines1 = f.readlines()

with open(file2) as f:
    lines2 = f.readlines()

lst = []
for i in range(len(lines1)):
    lst.append(lines1[i][:-1]+'\t'+lines2[i])

with open("./col12.txt", mode='w') as f:
    f.writelines(lst)
