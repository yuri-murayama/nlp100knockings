#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

path = 'nlp.txt.xml'
tree = ET.parse(path)
root = tree.getroot()
    
for name in root.iter('word'):
    print(name.text)

"""
./corenlp.sh -annotators tokenize,ssplit,pos,lemma,parse,ner,dcoref, --file nlp.txt
"""