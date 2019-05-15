import re

path = "output.txt"

with open(path) as f:
    lines = f.read()


pattern1 = re.compile(r"^\{\{基礎情報.*?$(.*?)^\}\}$", re.MULTILINE | re.DOTALL)

content = pattern1.findall(lines)

pattern2 = re.compile(r"^\|(.+?)\s*=\s*(.+?)((?=\n\|)|(?=\n$))", re.MULTILINE | re.DOTALL)

dict = {}

for c in content:
    m = pattern2.findall(c)

    for mm in m:
        mark = re.sub("\'{2,5}", "", mm[1])
        link = re.sub("\[\[([^\|]+\|)?([^\|]+?)\]\]", "\\2", mark)
        dict[mm[0]] = link
        print(mm[0], link)
