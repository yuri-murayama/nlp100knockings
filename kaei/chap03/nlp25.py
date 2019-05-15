import re

path = "output.txt"

with open(path) as f:
    lines = f.read()

pattern1 = re.compile(r"\{\{基礎情報.+?$(.+?)^\}\}", re.MULTILINE | re.DOTALL)

content = pattern1.search(lines)

pattern2 = re.compile(r"^\|(.+?)\s*=\s*(.+?)((?=\n\|)|(?=\n$))", re.MULTILINE | re.DOTALL)

dict = {}

m = pattern2.findall(content.group(1))

for mm in m:
    dict[mm[0]] = mm[1]
    print(mm[0], mm[1])
