#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

path = 'nlp.txt.xml'
tree = ET.parse(path)
root = tree.getroot()
    
for t_name in root.iter('token'):
    if t_name[5].text == 'PERSON':
        print(t_name[0].text)