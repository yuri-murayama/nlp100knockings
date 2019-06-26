#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from graphviz import Digraph

path = 'nlp.txt.xml'
tree = ET.parse(path)
root = tree.getroot()

# sentencesとedges
sen_lst = []
edge_lst = []

for sentence in root.iter('sentences'):
    for sen in sentence.iter('sentence'):
        words_lst = []
        dep_lst = []

        for tok in sen.iter('token'):
            words_lst.append(tok[0].text)
        sen_lst.append(words_lst)

        for dep in sen.iter('dependencies'):
            if dep.attrib['type']=='collapsed-dependencies':
                for de in dep.iter('dep'):
                    dep_lst.append([int(de[0].attrib['idx']), int(de[1].attrib['idx'])])
        edge_lst.append(dep_lst)


# グラフ
for i, words in enumerate(sen_lst):
    G = Digraph(format="png")
    G.attr("node", shape="circle")

    G.node('0', "ROOT")
    for j in range(len(words)): # ["Natural", "language", "processing", ...]
        G.node(str(j+1), words[j]) # 単語を一つずつインデックス付きで
    
    for d in edge_lst[i]: # [[0, 18], [3, 1], ...]
        G.edge(str(d[0]), str(d[1]))

    G.render("./tree/tree"+str(i+1))