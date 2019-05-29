# -*- coding: utf-8 -*-                                                        

with open('neko.txt.mecab','r') as f:
    ls = f.readlines()
#    print(ls)                                                                  
    for l in ls:
            p = l.split('\t')
            if len(p)>=2:
                p0 = p[1].split(',')
                nekodict = {'surface':p[0],'pos':p0[0],'pos1':p0[1],'base':p0[6\
]}
                if nekodict['pos'] == '動詞':
                    print(nekodict['surface'])
