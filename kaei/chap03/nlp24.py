import re

path = "output.txt"

with open(path) as f:
    lines = f.readlines()

pattern = re.compile(r"(File|ファイル):(.*?)\|")
lst = []

for line in lines:
    m = pattern.findall(line)
    if m:
        lst.append(m[0][1])

for l in lst:
    print(l)
