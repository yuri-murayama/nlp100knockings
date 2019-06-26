# -*- coding: utf-8 -*-

import re
import xml.etree.ElementTree as ET
tree = ET.parse('nlp.txt.xml')
root = tree.getroot()
word_lst=[]
pos_lst=[]
ner_lst=[]
for name in root.iter('word'):
    word_lst.append(name.text)
for name in root.iter('POS'):
    pos_lst.append(name.text)
for name in root.iter('NER'):
    ner_lst.append(name.text)

for (w,n,p) in zip(word_lst,ner_lst,pos_lst):
    if p=='NNP' and n=='PERSON':
        print('{}'.format(w))
