#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import re

path = 'nlp.txt.xml'
tree = ET.parse(path)
root = tree.getroot()

# 文章リスト、単語一つ一つが入っている
sen_lst = []
for sentence in root.iter('sentences'):
    for sen in sentence.iter('sentence'):
        words_lst = []
        for tok in sen.iter('token'):
            words_lst.append(tok[0].text)
        sen_lst.append(words_lst)

# 参照表現のリスト
# [[sentenceID, start, end, rep], ...]
core_lst = []
sen_start_lst = []
for c_block in root[0][2]:
    for m in c_block.iter('mention'):

        if len(m.attrib) > 0: # 代表参照表現の時
            rep = m[4].text
        
        else: # 参照表現の時
            if (int(m[0].text), int(m[1].text)) not in sen_start_lst: # 先に見つけた参照だけ
                core_lst.append([int(m[0].text), int(m[1].text), int(m[2].text), rep])
                sen_start_lst.append((int(m[0].text), int(m[1].text)))

# 参照表現を一つずつ置換
for core in core_lst:
    sen_lst[core[0]-1][core[1]-1] = '「'+core[3]+' ('+sen_lst[core[0]-1][core[1]-1] # 「rep  (s
    sen_lst[core[0]-1][core[2]-2] = sen_lst[core[0]-1][core[2]-2]+') 」' # e) 」

for sen in sen_lst:
    text = " ".join(sen)
    text = re.sub(r'-LRB-',r'(', text)
    text = re.sub(r'-RRB-',r')', text)
    text = re.sub(r'``\s',r'"', text)
    text = re.sub(r'\s\'\'',r'"', text)
    text = re.sub(r'\s\.',r'.', text)
    text = re.sub(r'\s,',r',', text)
    text = re.sub(r'\s\?',r'?', text)
    text = re.sub(r'\(\s',r'(', text)
    text = re.sub(r'\s\)',r')', text)
    print(text)