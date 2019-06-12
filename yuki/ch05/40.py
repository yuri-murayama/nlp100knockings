import re

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

cab = [] #文章の形態素解析が格納されている　１文が一つのリスト
sentence = []
with open('neko.txt.cabocha','r') as f:
    lines = f.readlines()  #read()だと１文字ずつ読み込んでしまう
    for line in lines:
        split_line = re.split(',|\t|\n|\s',line)
        if split_line[0] == '*':
            continue
        elif split_line[0] != 'EOS':
            sentence.append(Morph(split_line[0],split_line[7],split_line[1],split_line[2]))
        else:
            if len(sentence) != 0:
                cab.append(sentence)
            sentence = [] #sentenceの初期化

for cab in cab[1]:
    print(vars(cab))
