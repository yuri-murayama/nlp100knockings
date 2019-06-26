# -*- coding: utf-8 -*-

import re
import xml.etree.ElementTree as ET
tree = ET.parse('nlp.txt.xml')
root = tree.getroot()
word_lst=[]
lemma_lst=[]
pos_lst=[]
for name in root.iter('word'):
    word_lst.append(name.text)
for name in root.iter('lemma'):
    lemma_lst.append(name.text)
for name in root.iter('POS'):
    pos_lst.append(name.text)

for (w,l,p) in zip(word_lst,lemma_lst,pos_lst):
    print('{}\t{}\t{}\t'.format(w,l,p))

#print(pos_lst)
