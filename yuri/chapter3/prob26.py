from prob21 import fopen
import re

def to_text(l):
    l = re.sub(r'\'{2,5}', r'', l)
    return l

t = fopen()
pattern1 = r'基礎情報.*?^(.*?)^\}\}'
l = re.findall(pattern1, t, flags=re.MULTILINE | re.DOTALL)
pattern2 = r'^\|(.*?)\s\=\s(.*?)$'
l = re.findall(pattern2, l[0], flags=re.MULTILINE)
d = {line[0]: to_text(line[1]) for line in l}

for k, v in d.items():
    print(k, v)