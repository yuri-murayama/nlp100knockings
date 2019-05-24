#二つの名詞が　の　で連結されている名詞句を抽出する 
import re
dic = {}
lis = []
flag = 0
with open('neko.txt.mecab','r') as f:
    lines = f.readlines()  #read()だと１文字ずつ読み込んでしまう                    
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
                for i in range(len(lis)-2):
                    if lis[i]['pos'] == '名詞' and lis[i+1]['surface'] == 'の' and lis[i+2]['pos'] == '名詞':
                        print(lis[i]['surface']+'の'+lis[i+2]['surface'])
            lis = []




