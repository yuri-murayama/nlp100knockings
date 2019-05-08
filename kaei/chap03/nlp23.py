import re

path = "output.txt"

with open(path) as f:
    lines = f.readlines()

pattern = re.compile(r"^(=+)(.+?)(=+)$")

for line in lines:
    m = pattern.match(line)
    if m is not None:
        print("{0}:{1}".format(m.group(2), m.group(1).count('=')))
