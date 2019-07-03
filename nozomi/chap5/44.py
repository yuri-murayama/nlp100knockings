# -*- coding: utf-8 -*-
import re
import pydot
from graphviz import Digraph

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface =  surface
        self.base    =  base
        self.pos     =  pos
        self.pos1    =  pos1

class Chunk:
    def __init__(self,morphs,srcs,dst):
        self.morphs = morphs
        self.srcs = srcs
        self.dst = dst
    def __str__(self):
        p = []
        for morph in self.morphs:
            p.append(morph.surface)
        return '{}{}'.format("".join(p),self.dst)

def mklst(rl):
    lst0 = []
    for chunk in rl:
        if chunk.dst != -1:
            moto = ''.join([morph.surface.strip('。') for morph in chunk.morphs])
            saki = ''.join([morph.surface.strip('。') for morph in rl[chunk.dst].morphs])
            lst0.append((moto,saki))
    return lst0

def keitaiso():
    sentences = []
    sentence = []
    chunk = None
    lst = {}
    with open('neko.txt.cabocha','r') as f:
        for line in f:
            if line[0] == '*':
                if chunk is not None:
                    sentence.append(chunk)
                l_lst = line.split(' ')
                dst = int(l_lst[2].strip('D'))
                srcs = l_lst[1]
                if dst in lst.keys():
                    lst[dst].append(srcs)
                else:
                    lst[dst] = [srcs]
                morphs = []
                chunk = Chunk(morphs,srcs,dst)
            elif line[0:4] == 'EOS\n':
                if chunk is not None:
                    sentence.append(chunk)
                if len(sentence) > 0:
                    sentences.append(sentence)
                for i,chunk in enumerate(sentence):
                    #print(lst.keys())
                    if i in lst.keys():
                        chunk.srcs = lst[i]
                    else:
                        chunk.srcs = []

                chunk = None
                sentence = []
                lst = {}
            else:
                l_lst2 = line.split('\t')
                #print(l_lst2)
                l_lst3 = l_lst2[1].split(',')
                mo = Morph(surface=l_lst2[0], base=l_lst3[6], pos=l_lst3[0], pos1=l_lst3[1])
                chunk.morphs.append(mo)


    return sentences


if __name__ == '__main__':
    ke = keitaiso()
    lst = mklst(ke[3])
    G = pydot.Dot(graph_type='digraph')
    G.set_node_defaults(shape='box')
    for l in lst:
        G.add_edge(pydot.Edge(l[0], l[1]))
    G.write_png('output44.png')
