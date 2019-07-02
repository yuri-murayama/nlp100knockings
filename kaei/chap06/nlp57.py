#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from graphviz import Digraph

path = 'nlp.txt.xml'
tree = ET.parse(path)
root = tree.getroot()

# 全文のリスト
sen_lst = []
edge_lst = []
del_lst = [] # あとでノードから外すもの

for sentence in root.iter('sentences'):
    for sen in sentence.iter('sentence'):
        # 一文ごとのリスト
        words_lst = []
        dep_lst = []
        del_part_lst = []

        for tok in sen.iter('token'):
            words_lst.append(tok[0].text)
        sen_lst.append(words_lst)

        for d in range(len(words_lst)):
            del_part_lst.append(d+1) # [1, 2, ...] edgeのindexと一緒

        for dep in sen.iter('dependencies'):
            if dep.attrib['type']=='collapsed-dependencies':
                for de in dep.iter('dep'):
                    if de.attrib['type']!='punct':
                        dep_lst.append([int(de[0].attrib['idx']), int(de[1].attrib['idx'])])
                        if int(de[0].attrib['idx']) in del_part_lst:
                            del_part_lst.remove(int(de[0].attrib['idx']))
                        if int(de[1].attrib['idx']) in del_part_lst:
                            del_part_lst.remove(int(de[1].attrib['idx']))
        edge_lst.append(dep_lst)
        del_lst.append(del_part_lst)

# グラフ
for i, words in enumerate(sen_lst):
    G = Digraph(format="png")
    G.attr("node", shape="circle")

    G.node('0', "ROOT")
    for j in range(len(words)): # ["Natural", "language", "processing", ...]
        if j+1 not in del_lst[i]:
            G.node(str(j+1), words[j]) # 単語を一つずつインデックス付きで
    
    for d in edge_lst[i]: # [[0, 18], [3, 1], ...]
        G.edge(str(d[0]), str(d[1]))

    G.render("./tree/tree"+str(i+1))