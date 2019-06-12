# -*- coding: utf-8 -*-                                                     

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface =  surface
        self.base    =  base
        self.pos     =  pos
        self.pos1    =  pos1

with open('neko.txt.cabocha','r') as f:
    ls = f.readlines()
    lst = []
    lsls = []
    for l in ls:
        if l == 'EOS\n':
            #print(lst)
            lsls.append(lst)
            lst = []
        else:
            p = l.split('\t')
            if len(p)>=2:
                p0 = p[1].split(',')
                m = Morph(p[0],p0[6],p0[0],p0[1])
                lst.append(m)

for m in lsls[2]:
    print(vars(m))
