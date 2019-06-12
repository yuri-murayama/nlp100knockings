# -*- coding: utf-8 -*-  
import re

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
        self.dst = int(dst.strip('D'))
#    def __str__(self):

def keitaiso():
    sentences = []
    sentence = []
    chunk = None
    with open('neko.txt.cabocha','r') as f:
        for line in f:
            #l_lst = line.split()
            #if l_lst[0] != '*' and l_lst[0] != 'EOS':
            if line[0] == '*':
                l_lst = line.split(' ')
                dst = l_lst[2]
                srcs = l_lst[1]
                lst = {}
                #lst[dst] = srcs
                if dst in lst.keys():
                    lst[dst].append(srcs)
                else:
                    lst[dst] = [srcs]
                if chunk is not None:
                    chunk = Chunk(morphs,dst,srcs)
            elif line[0] == 'EOS': 
                if chunk is not None:
                    sentence.append(chunk)
                if len(sentence) > 0:
                    sentences.append(sentence)
                chunk = None
                sentence = []
            else:
                l_lst2 = line[0].split(',') + line[1].split(',')
                mo = Morph(surface=l_lst2[0], base=l_lst2[7], pos=l_lst2[1], pos1=l_lst2[2])
                chunk.morphs.append(mo)
                
#            else:
#                ls = l_lst.split('\t')
#                ls2 = ls[1].split(',')



    return sentences

for m in keitaiso()[7]:
    print(m)
#for i, cs in enumerate(keitaiso()):
#    if i == 7:
#        for j, ck in enumerate(cs):
#            print(ck)
#        break
