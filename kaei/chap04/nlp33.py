#-*- coding: utf-8 -*-

import nlp30

def noun_sa(lst):
    for l in lst: # 1文
        for ll in l: # 1語
            if ll['pos'] == "名詞":
                if ll['pos1'] == "サ変接続":
                    print(ll['surface'], ll['base'])

if __name__=='__main__':
    lst = nlp30.make_lst()
    noun_sa(lst)
