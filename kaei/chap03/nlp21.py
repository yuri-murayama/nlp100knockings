import re

path = "output.txt"

with open(path) as f:
    lines = f.readlines()

pattern = re.compile(r"^(\[\[Category:)(.+)(\]\])$")

for line in lines:
    m = pattern.match(line)
    if m is not None:
        print(m.group())
