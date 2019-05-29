# -*- coding: utf-8 -*-                                                              \                                                                                      
with open('neko.txt.mecab','r') as f:
    ls = f.readlines()
    lst = []
#    print(ls)                                                                        
    for l in ls:
        if l == 'EOS\n':
#            print(lst)                                                               
            for x in range(len(lst)-1):
                if lst[x-1]['pos']=='名詞' and lst[x]['pos']=='名詞' and lst[x+1]['pos']=='名詞':
                    print(lst[x-1]['surface'] + lst[x]['surface'] + lst[x+1]['surface'])
                if lst[x]['pos']=='名詞' and lst[x+1]['pos']=='名詞':
                    print(lst[x]['surface'] + lst[x+1]['surface'])
                   # x0 = lst[x]['surface']
            lst = []
        else:
            p = l.split('\t')
            if len(p)>=2:
                p0 = p[1].split(',')
                nekodict = {'surface':p[0],'base':p0[6],'pos':p0[0],'pos1':p0[1\
]}
                lst.append(nekodict)
