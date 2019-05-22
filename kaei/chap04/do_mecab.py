import sys
import MeCab

m = MeCab.Tagger()

with open("neko.txt") as f:
    lines = f.read()

result = m.parse(lines)

with open("neko.txt.mecab","w") as ff:
    ff.write(result)
