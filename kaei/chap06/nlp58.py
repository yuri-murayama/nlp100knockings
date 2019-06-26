#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from graphviz import Digraph

path = 'nlp.txt.xml'
tree = ET.parse(path)
root = tree.getroot()

for deps in root.iter('dependencies'):

    # 1文ごとに辞書作成
    nsubj_dic = {}
    dobj_dic = {}
    if deps.attrib['type']=='collapsed-dependencies':
        for dep in deps.iter('dep'): # <dep>ごとに見る
            if dep.attrib['type']=='nsubj':
                nsubj_dic[dep[0].text] = dep[1].text

            elif dep.attrib['type']=='dobj':
                dobj_dic[dep[0].text] = dep[1].text
    
    # 1文ごとにprint
    for key in  nsubj_dic.keys():
        if key in dobj_dic:
            print("{0}\t{1}\t{2}".format(nsubj_dic[key], key, dobj_dic[key]))
