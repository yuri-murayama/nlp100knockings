from prob21 import fopen
import re

t = fopen()
pattern = r'(?:ファイル|File):(.*?)\|'
l = re.findall(pattern, t)
print(l)