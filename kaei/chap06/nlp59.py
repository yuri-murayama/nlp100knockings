#-*- coding: utf-8 -*-

# 参考 : https://stackoverflow.com/questions/5454322/python-how-to-match-nested-parentheses-with-regex/12280660#12280660

import xml.etree.ElementTree as ET
import regex as re # 再帰的な検索可能ライブラリ

path = 'nlp.txt.xml'
tree = ET.parse(path)
root = tree.getroot()

pattern = re.compile(r'(?<rec>\((?:[^()]+|(?&rec))*\))') # ()の無い文字列 | それ自体
pattern2 = re.compile(r'\(.+?\s([^()]+?)\)')

for s in root.iter('parse'):
    m = pattern.search(s.text)
    result = m.captures('rec')
   
    for r in result:
        if r[1:3] == 'NP':
            m2 = pattern2.findall(r)
            print(" ".join(m2))