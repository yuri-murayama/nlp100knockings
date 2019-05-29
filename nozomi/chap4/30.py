# -*- coding: utf-8 -*-   

with open('neko.txt.mecab','r') as f:
    ls = f.readlines()
    lst = []
#    print(ls)
    for l in ls:
        if l == 'EOS\n':
            print(lst)
            lst = []
        else:
            p = l.split('\t')
            if len(p)>=2:
                p0 = p[1].split(',')
                nekodict = {'surface':p[0],'base':p0[6],'pos':p0[0],'pos1':p0[1]}
                lst.append(nekodict)
#            while nekodict['surface']=='。':
#        print(lst)
#        print(p)
#        print(s)
#        l.split(',')
#        l.split('\n')
#        print(l[0].strip('\n'))
