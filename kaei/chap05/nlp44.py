#-*- coding: utf-8 -*-

import nlp40
import nlp41
from graphviz import Digraph
import CaboCha
import re

def make_chunk(lines):
    lst = []
    class_lst = []
    sen_lst = []
    chunk_lst = []
    srcs_dic = {}
    dst_lst = []

    for line in lines:
        # 文末
        if line=='EOS\n':
            if len(chunk_lst)>0:
                sen_lst.append(chunk_lst)

            chunk_lst = []

            if len(sen_lst)>0:
                for i, ch in enumerate(sen_lst):
                    key = str(i) + 'D'
                    if key in srcs_dic:
                        srcs = srcs_dic[key]
                    else:
                        srcs = []

                    chunk = nlp41.Chunk(ch, dst_lst[i], srcs)
                    class_lst.append(chunk)

                lst.append(class_lst)
            class_lst = []
            sen_lst = []
            srcs_dic = {}
            dst_lst = []
            
        else:
            if line[0]=='*':
                if len(chunk_lst)>0:
                    sen_lst.append(chunk_lst)
                
                chunk_lst = []

                # 係り元情報の記憶
                l = line.strip().split(' ')
                if l[2] in srcs_dic.keys():
                    srcs_dic[l[2]] = srcs_dic[l[2]]+[l[1]]
                else:
                    srcs_dic[l[2]] = [l[1]]
                
                dst_lst.append(l[2][:-1])
                
            else:
                line = line.strip().split('\t')
                # 空白のとき
                if len(line)==1: # ここの長さだけ変更
                    surface = ' '
                    l = line[0].split(',')
                else:
                    surface = line[0]
                    l = line[1].split(',')

                #print(l)
                word = nlp40.Morph(surface, l[6], l[0], l[1])
                chunk_lst.append(word)

    return lst

if __name__=='__main__':
    # 入力文
    sentence = input()
    
    # CaboCha関連
    c = CaboCha.Parser()
    tree = c.parse(sentence)

    lines = tree.toString(CaboCha.FORMAT_LATTICE)
    contents = re.findall(r'.*\n', lines, re.MULTILINE)

    lst = make_chunk(contents)[0]

    G = Digraph(format="png")
    G.attr("node", shape="circle")

    for i in range(len(lst)):
        G.node(str(i), "".join([morph.surface for morph in lst[i].morphs]))
    
    for i in range(len(lst)):
        if lst[i].dst != '-1':
            G.edge(str(i), str(lst[i].dst))
    
    G.render('tree')