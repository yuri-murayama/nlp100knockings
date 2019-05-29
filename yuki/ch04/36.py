#出現頻度が高い１０語とその出現頻度を求め出現頻度の高い順に並べよ

import re
from collections import Counter
dic = {}
lis = []
flag = 0
with open('neko.txt.mecab','r') as f:
    lines = f.readlines()  #read()だと１文字ずつ読み込んでしまう
    wordcou = Counter()
    for line in lines:
        sline = re.split(',|\t|\n',line)
        if sline[0] != 'EOS':
            lis.append(dic)
            dic['surface'] = sline[0]
            dic['base'] = sline[7]
            dic['pos'] = sline[1]
            dic['pos1'] = sline[2]
            dic = {}
            flag = 0
        else:
            flag += 1
            if flag != 2:
                wordcou.update([dic['surface'] for dic in lis])
            lis = []
    lisword = wordcou.most_common()
    print(lisword)
