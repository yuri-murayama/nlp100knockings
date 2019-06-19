#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

path = 'nlp.txt.xml'
tree = ET.parse(path)
root = tree.getroot()
    
for t_name in root.iter('token'):
    output = []
    output.append(t_name[0].text)
    output.append(t_name[1].text)
    output.append(t_name[4].text)

    print("\t".join(output))