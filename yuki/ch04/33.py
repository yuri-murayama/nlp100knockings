#サ変接続の名詞を抽出

import re
dic = {}
lis = []
with open('neko.txt.mecab','r') as f:
    lines = f.readlines()  #read()だと１文字ずつ読み込んでしまう                    

    for line in lines:
        sline = re.split(',|\t|\n',line)
        if sline[0] != 'EOS':
            if sline[1] == '名詞' and sline[2] == 'サ変接続':
                print(sline[0])
