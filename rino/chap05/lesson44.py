# -*- coding: utf-8 -*-
# 参考サイト: https://qiita.com/shimo_t/items/b761973805f2cf0b2967

import CaboCha
from lesson41 import getChunkCabocha
from graphviz import Digraph

sentence = input()

c = CaboCha.Parser()
tree =  c.parse(sentence)

print(tree.toString(CaboCha.FORMAT_LATTICE))
chunk_list = getChunkCabocha(tree.toString(CaboCha.FORMAT_LATTICE))[0]

# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
G = Digraph(format='png')
G.attr('node', shape='circle')

N = len(chunk_list)  # ノード数

# ノードの追加
for i in range(N):
    chunk_label = "".join([m.surface for m in chunk_list[i].morphs])
    G.node(str(i), chunk_label)

for i in range(N):
    if chunk_list[i].dst !=  str(-1):
        G.edge(str(i), str(chunk_list[i].dst))

# binary_tree.pngで保存
G.render('tree')
