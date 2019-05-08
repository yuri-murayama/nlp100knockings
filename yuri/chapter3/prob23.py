from prob21 import fopen
import re

t = fopen()
pattern = r'^(=+)(.*?)=+$'
l = re.findall(pattern, t, flags=re.MULTILINE)
d = {line[1]: len(line[0]) for line in l}

for k, v in d.items():
    print('セクション名:{0} レベル:{1}'.format(k, v))