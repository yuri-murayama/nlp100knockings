#名詞の連接を最長一致で抽出する

import re
dic = {}
lis = []
flag = 0
ans = []
cou = 0
n = ''
hold = ''

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
                for i in range(len(lis)):
                    if lis[i]['pos'] == '名詞':
                        cou += 1
                        n= n + lis[i]['surface']
                        if i == (len(lis)-1) and len(n) > 1:
                            hold = n
                            n = ''
                            cou = 0
                            if hold != '':
                                ans.append(hold)
                    else:
                        if cou > 1:
                            hold = n
                            cou = 0
                            n = ''
                            if hold != '':
                                ans.append(hold)
                        else:
                            n = ''
                            cou = 0
                        
            lis = []
    print(ans)
#    print(ans)
