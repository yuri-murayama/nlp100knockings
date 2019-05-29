#36のトップ10こをグラフで表す
import re
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib as mpl
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
    lisword = wordcou.most_common(10)
    left = [w for (w,c) in lisword]
    height = [c for (w,c) in lisword]
    plt.bar(left, height)
    plt.xlabel("頻出単語")
    plt.ylabel("出現回数")
    plt.show()
#    print(left)
#    print(lisword)





