# -*- coding: utf-8 -*-

import re
import xml.etree.ElementTree as ET
import pydot
from graphviz import Digraph

tree = ET.parse('nlp2.txt.xml')
root = tree.getroot()
governor_lst=[]
dependent_lst=[]


for name0 in root.iter('sentence'):
    if name0.get('id')=='1':
        for name in name0.iter('dependencies'):
            #print(name.attrib)
            if name.get('type')=='collapsed-dependencies':
                for name2 in name.iter('governor'):
                    governor_lst.append(name2.text)
                for name3 in name.iter('dependent'):
                    dependent_lst.append(name3.text)
    else:
        break;

edges = list(zip(governor_lst,dependent_lst))

#print(edges)
G = Digraph(format="png")
G.attr("node", shape="box")
for i,j in edges:
    G.edge(str(i), str(j))
G.render("output57-1")
