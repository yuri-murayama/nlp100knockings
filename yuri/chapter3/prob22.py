from prob21 import fopen
import re

t = fopen()
pattern = r'Category:(.*?)(?:\|\*)*\]'
l = re.findall(pattern, t)
print(l)